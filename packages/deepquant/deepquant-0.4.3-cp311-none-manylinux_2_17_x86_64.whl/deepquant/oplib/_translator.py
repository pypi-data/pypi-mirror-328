import ast
import inspect
from types import FunctionType, FrameType
from typing import Dict, List, Any, Optional, Union
from enum import Enum
from ._swordfishcpp import FunctionDef, Constant, create_partial, Void
from ._swordfishcpp._tools import check_builtin_function, check_is_nothing
import uuid


Nothing = Void.VOID_VALUE
DFLT = Void.DFLT_VALUE


def _generate_name():
    return f"TMP_TRS_{uuid.uuid4().hex[:8]}"


class VariableMode(Enum):
    PYTHON = 0
    SWORDFISH = 1
    DELETE = 2


class Variable:
    def __init__(self, visitor, data, mode: VariableMode) -> None:
        self.visitor: StatementVisitor = visitor
        self.data = data
        self.mode = mode

    def dot(self, o: str):
        if self.mode == VariableMode.PYTHON:
            return Variable(self.visitor, getattr(self.data, o), VariableMode.PYTHON)
        elif self.mode == VariableMode.SWORDFISH:
            return Variable(self.visitor, str(self) + f".{o}", VariableMode.SWORDFISH)
        else:
            raise ValueError("Invalid Statement.")

    def __str__(self):
        if self.mode == VariableMode.PYTHON:
            if isinstance(self.data, FunctionDef) and check_builtin_function(self.data):
                return str(self.data)
            return self.visitor.update_argvar(self)
        return str(self.data)


class VariableFrame:
    data: Dict[str, Variable]

    def __init__(self, visitor, vars_dict: Dict[str, Any] = None):
        self.data = dict()
        if vars_dict:
            for n, v in vars_dict.items():
                self.data[n] = Variable(visitor, v, VariableMode.PYTHON)

    def update(self, name: str, value: Variable):
        self.data[name] = value

    def find(self, name: str) -> Union[Variable, None]:
        if name in self.data:
            return self.data[name]
        else:
            return None

    @classmethod
    def createArgsFrame(cls, visitor, args: set):
        frame = VariableFrame(visitor)
        for arg in args:
            frame.update(arg, Variable(visitor, arg, VariableMode.SWORDFISH))
        return frame


class FrameStack:
    stack: List[VariableFrame]

    def __init__(self, visitor):
        self.visitor = visitor
        self.stack = []

    def push(self, frame: Optional[VariableFrame] = None):
        if frame:
            self.stack.append(frame)
        else:
            self.stack.append(VariableFrame(self.visitor))

    def pop(self):
        self.stack.pop()

    def add(self, name: str, value: Variable):
        self.stack[-1].update(name, value)

    def find(self, name: str) -> Union[Variable, None]:
        for frame in reversed(self.stack):
            res = frame.find(name)
            if res:
                return res
        return None


class StatementVisitor(ast.NodeVisitor):
    def __init__(self, func: FunctionType, frame: FrameType):
        self.stack = FrameStack(self)
        self.var_dict: Dict[str, Constant] = dict()
        self.rev_dict: Dict[int, str] = dict()
        self.stack.push(VariableFrame(self, frame.f_globals))
        self.stack.push(VariableFrame(self, frame.f_locals))
        signature = inspect.signature(func)
        params = set(signature.parameters.keys())
        self.stack.push(VariableFrame.createArgsFrame(self, params))

    def update_argvar(self, var: Variable):
        if var.data in self.rev_dict:
            return self.rev_dict[id(var.data)]
        name = _generate_name()
        self.var_dict[name] = var.data
        self.rev_dict[id(var.data)] = name
        return name

    def visit_arguments(self, node: ast.arguments):
        if node.posonlyargs:
            raise ValueError("unsupport position only args.")
        if node.kwonlyargs or node.kw_defaults:
            raise ValueError("unsupport keyword only args.")
        all_args_len = len(node.args)
        all_defaults_len = len(node.defaults)
        index = 0
        arg_statements = []
        defaults = node.defaults
        non_defaults = all_args_len - all_defaults_len
        for arg in node.args:
            if index < non_defaults:
                arg_statements.append(arg.arg)
            else:
                arg_statements.append(f"{arg.arg} = {str(self.visit(defaults[index - non_defaults]))}")
            index += 1
        if not arg_statements:
            return []
        return arg_statements

    def visit_Lambda(self, node: ast.Lambda):
        args = self.visit_arguments(node.args)
        body = str(self.visit(node.body))
        return f"(def ({', '.join(args)}) -> {body})"

    def visit_Name(self, node: ast.Name):
        if isinstance(node.ctx, ast.Load):
            res = self.stack.find(node.id)
            if res:
                return res
            else:
                raise ValueError("use undefined variable: " + node.id + ".")
        elif isinstance(node.ctx, ast.Store):
            var = Variable(self, node.id, VariableMode.SWORDFISH)
            self.stack.add(node.id, var)
            return var
        else:   # node.ctx == ast.Del()
            raise ValueError("unsupport delete statement.")
            # return Variable(self, f"del {node.id}", VariableMode.DELETE)

    def visit_Constant(self, node: ast.Constant):
        value = node.value
        if value is None:
            return "NULL"
        if isinstance(value, str):
            chs = []
            for ch in value:
                if ch in ['"', "'"]:
                    chs.append("\\")
                chs.append(ch)
            return f'"{"".join(chs)}"'
        if isinstance(value, bool):
            return str(value).lower()
        if isinstance(value, int):
            return str(value)
        if isinstance(value, float):
            return str(value)
        # bytes, complex, Ellipsis
        raise RuntimeError("unsupport")

    def visit_Tuple(self, node: ast.Tuple):
        sub_objs = []
        for sub_node in node.elts:
            sub_objs.append(str(self.visit(sub_node)))
        return f"({', '.join(sub_objs)})"

    def visit_List(self, node: ast.List):
        sub_objs = []
        for sub_node in node.elts:
            sub_objs.append(str(self.visit(sub_node)))
        return f"[{', '.join(sub_objs)}]"

    def visit_Set(self, node: ast.Set):
        sub_objs = []
        for sub_node in node.elts:
            sub_objs.append(str(self.visit(sub_node)))
        return f"set([{', '.join(sub_objs)}])"

    def visit_Dict(self, node: ast.Dict):
        key_objs = []
        for key in node.keys:
            key_objs.append(str(self.visit(key)))
        val_objs = []
        for val in node.values:
            val_objs.append(str(self.visit(val)))
        return f"dict([{', '.join(key_objs)}], [{', '.join(val_objs)}], false)"

    def visit_Attribute(self, node: ast.Attribute):
        attr: Variable = self.visit(node.value).dot(node.attr)
        if isinstance(node.ctx, ast.Store):
            if attr.mode == VariableMode.PYTHON:
                raise ValueError("unsupport Attribute assign.")
        return attr

    def visit_Subscript(self, node: ast.Subscript):
        value: Variable = self.visit(node.value)
        if isinstance(node.ctx, ast.Store):
            if value.mode == VariableMode.PYTHON:
                raise ValueError("unsupport Subscript assign.")
        slice = self.visit(node.slice)
        return f"{str(value)}[{str(slice)}]"

    def visit_Index(self, node: ast.Index) -> Any:
        return self.visit(node.value)

    def visit_ExtSlice(self, node: ast.ExtSlice) -> Any:
        return ",".join([self.visit(dim) for dim in node.dims])

    def visit_Slice(self, node: ast.Slice) -> Any:
        lower = str(self.visit(node.lower)) if node.lower else ""
        upper = str(self.visit(node.upper)) if node.upper else ""
        if node.step:
            raise ValueError("unsupport step in slice.")
        return f"{lower}:{upper}"

    def visit_Call(self, node: ast.Call):
        func: Variable = self.visit(node.func)
        func_str = ""
        if func.mode == VariableMode.PYTHON:
            if isinstance(func.data, Constant):
                func_str = str(func)
            else:
                raise ValueError("Unsupport other python variables.")
        elif func.mode == VariableMode.SWORDFISH:
            func_str = str(func)
        else:
            raise ValueError("Invalid variable mode.")
        args = [str(self.visit(_arg)) for _arg in node.args]
        kwargs = [f"{k.arg}={str(self.visit(k.value))}" for k in node.keywords]
        all_args = ",".join(args + kwargs)
        return f"{func_str}({all_args})"

    def visit_Assign(self, node: ast.Assign):
        value_str = str(self.visit(node.value))
        target_str: str = ""
        for target in node.targets:
            tmp_str: str
            if isinstance(target, ast.Tuple):
                tmp_str = ", ".join([str(self.visit(sub_node)) for sub_node in target.elts])
            elif isinstance(target, ast.Name):
                tmp_str = str(self.visit_Name(target))
            else:
                raise RuntimeError("unsupport")
            target_str += f"{tmp_str} = {value_str};\n"
        return target_str

    def visit_AugAssign(self, node: ast.AugAssign):
        value_str = str(self.visit(node.value))
        target_str = str(self.visit(node.target))
        op_str = str(self.visit(node.op))
        return f"{target_str} {op_str}= {value_str};\n"

    def visit_If(self, node: ast.If):
        test = str(self.visit(node.test))
        self.stack.push()
        body = [str(self.visit(b)) for b in node.body]
        self.stack.pop()
        orelse = [str(self.visit(o)) for o in node.orelse]
        return f"""
        if ({test}) {{
            {"".join(body)}
        }}
        else {{
            {"".join(orelse)}
        }}
        """

    def visit_For(self, node: ast.For):
        target: Variable = self.visit(node.target)
        iter: Variable = self.visit(node.iter)
        self.stack.push()
        self.stack.add(str(target), target)
        self.stack.push()
        body = [str(self.visit(b)) for b in node.body]
        self.stack.pop()
        if node.orelse:
            raise ValueError("unsupport for-else statement.")
        res = f"""
            for ({str(target)} in {str(iter)}) {{
                {"".join(body)}
            }}
        """
        self.stack.pop()
        return res

    def visit_While(self, node: ast.While):
        test = self.visit(node.test)
        self.stack.push()
        body = [str(self.visit(b)) for b in node.body]
        if node.orelse:
            raise ValueError("unsupport for-else statement.")

        check_var = _generate_name()
        res = f"""
            {check_var} = true;
            do {{
                if ({check_var}) {{
                    {check_var} = false;
                    continue;
                }}
                {"".join(body)}
            }}
            while ({test});
        """
        self.stack.pop()
        return res

    def visit_Break(self, node: ast.Break):
        return "break;\n"

    def visit_Continue(self, node: ast.Continue):
        return "continue;\n"

    def visit_Return(self, node: ast.Return):
        return f"return {str(self.visit(node.value))};"

    def visit_Expr(self, node: ast.Expr):
        if isinstance(node.value, ast.Name):
            raise RuntimeError("unsupport")
        return str(self.visit(node.value)) + ";\n"

    def visit_Compare(self, node: ast.Compare):
        left = str(self.visit(node.left))
        ops = [self.visit(op) for op in node.ops]
        comps = [str(self.visit(c)) for c in node.comparators]
        compare_str = left
        for op, comp in zip(ops, comps):
            compare_str += f" {op} {comp}"
        return compare_str

    def visit_BoolOp(self, node: ast.BoolOp):
        op = self.visit(node.op)
        values = [str(self.visit(value)) for value in node.values]
        return "(" + f" {op} ".join(values) + ")"

    def visit_UnaryOp(self, node: ast.UnaryOp):
        op = self.visit(node.op)
        operand = self.visit(node.operand)
        return f"({op} {operand})"

    def visit_BinOp(self, node: ast.BinOp):
        L = self.visit(node.left)
        R = self.visit(node.right)
        op = self.visit(node.op)
        return f"({L} {op} {R})"

    # --------------------------------------
    # --- cmpop
    def visit_Eq(self, node: ast.Eq):
        return "=="

    def visit_Gt(self, node: ast.Gt):
        return ">"

    def visit_GtE(self, node: ast.GtE):
        return ">="

    def visit_In(self, node: ast.In):
        return "in"

    def visit_Is(self, node: ast.Is):
        raise ValueError("unsupport Is compare.")

    def visit_IsNot(self, node: ast.IsNot):
        raise ValueError("unsupport IsNot compare.")

    def visit_Lt(self, node: ast.Lt):
        return "<"

    def visit_LtE(self, node: ast.LtE):
        return "<="

    def visit_NotEq(self, node: ast.NotEq):
        return "!="

    def visit_NotIn(self, node: ast.NotIn):
        raise ValueError("unsupport NotIn compare.")

    # --------------------------------------
    # --- boolOp
    def visit_And(self, node: ast.And):
        return "and"

    def visit_Or(self, node: ast.Or):
        return "or"

    # --------------------------------------
    # --- UnaryOp
    def visit_Invert(self, node: ast.Invert):
        return "bitNot"

    def visit_Not(self, node: ast.Not):
        return "!"

    def visit_UAdd(self, node: ast.UAdd):
        return "+"

    def visit_USub(self, node: ast.USub):
        return "-"

    # --------------------------------------
    # --- BinOp
    def visit_Add(self, node: ast.Add):
        return "+"

    def visit_BitAnd(self, node: ast.BitAnd):
        return "&"

    def visit_BitOr(self, node: ast.BitOr):
        return "|"

    def visit_BitXor(self, node: ast.BitXor):
        return "^"

    def visit_Div(self, node: ast.Div):
        # TODO: need check
        return "\\"

    def visit_FloorDiv(self, node: ast.FloorDiv):
        return "/"

    def visit_LShift(self, node: ast.LShift):
        return "<<"

    def visit_Mod(self, node: ast.Mod):
        return "%"

    def visit_Mult(self, node: ast.Mult):
        return "*"

    def visit_MatMult(self, node: ast.MatMult):
        return "**"

    def visit_Pow(self, node: ast.Pow):
        return "pow"

    def visit_RShift(self, node: ast.RShift):
        return ">>"

    def visit_Sub(self, node: ast.Sub):
        return "-"


def _translate_wrapper(func: FunctionType, frame: FrameType, is_aggregation: bool = False):
    source_lines, line_nums = inspect.getsourcelines(func)

    if source_lines:
        s = source_lines[0]
        if s.startswith(" "):
            num_spaces = len(s) - len(s.lstrip(' '))
            source_lines = [line[num_spaces:] for line in source_lines]
    func_code = "".join(source_lines)

    func_node = ast.parse(func_code).body[0]

    statements = []
    statement_visitor = StatementVisitor(func, frame)
    args = statement_visitor.visit_arguments(func_node.args)
    for statement in func_node.body:
        code = statement_visitor.visit(statement)
        statements.append(code)

    vars_args = list(statement_visitor.var_dict.keys())
    args_str = ",".join(vars_args + args)

    function_body = "".join(statements)
    function_head = "defg" if is_aggregation else "def"
    function_code = f"""
    {function_head} ({args_str}) {{
        {function_body}
    }}
    """
    functiondef = FunctionDef(function_code)
    args = list(statement_visitor.var_dict.values())
    if args:
        args = [DFLT if isinstance(arg, Constant) and check_is_nothing(arg) else arg for arg in args]
        return create_partial(functiondef, *args)
    return functiondef


__all__ = [
    "_translate_wrapper",
]
