from llvmlite import ir

module = ir.Module(name = 'my_module')
func_type = ir.FunctionType(ir.IntType(32) , [])
func = ir.Function(module , func_type , name='main')
block = func.append_basic_block(name = 'entry')
builder = ir.IRBuilder(block)

x = ir.Constant(ir.IntType(32) , 5)
y = ir.Constant(ir.IntType(32) , 3)
result = builder.add(x , y)
builder.ret(result)

print(module)
