# run_chain.py
from tasks import calc
from celery import chain
 
subtask_1 = calc.add.s( 1, 2 )
subtask_2 = calc.add.s( 3 )
subtask_3 = calc.add.s( 4 )
subtask_4 = calc.add.s( 5 )
 
# 튜플 또는 리스트를 이용한 Chain
# tasks = ( subtask_1, subtask_2, subtask_3, subtask_4 )
 
# 비트연산자를 이용한 Chain
# tasks = subtask_1 | subtask_2 | subtask_3 | subtask_4 
 
# chaining = chain( tasks )   # Chain Task 생성
# chain_task = chaining( )    # Chain 실행

chain_task = ( subtask_1 | subtask_2 | subtask_3 | subtask_4 ).apply_async()
 
print( "\n# 1. Task ID 확인" )
print( "chain_task is {}".format( chain_task.id ) )
 
print( "\n# 2. Task 상태" )
print( "chain_task is {}".format( chain_task.ready() ) )
 
print( "\n# 3. 실행결과 확인" )
print( "chain_task is {}".format( chain_task.get() ) )
 
print( "\n# 4. Task 상태" )
print( "chain_task is {}".format( chain_task.ready() ) )