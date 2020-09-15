# run_chain.py
from tasks import calc
from celery import chord

tasks = [ calc.add.s( i, i+1 ) for i in range(1, 5) ]

chording = chord( tasks )
chord_task = chording( calc.callback.s() )
 
print( "\n# 1. Task 확인" )
print( "tasks = {}".format( tasks ) )
print( "chord_task.id = {}".format( chord_task.id ) )
print( "chord_task.type = {}".format( type(chord_task) ) )
 
print( "\n# 2. Task 상태 확인" )
print( "Subtask가 모두 준비되었는가? {}".format( chord_task.ready() ) )
 
print( "\n# 3. 실행결과 확인" )
print( "완료된 결과를 반환. {}".format( chord_task.get() ) )
 
print( "\n# 4. Task 상태 확인" )
print( "Subtask가 모두 준비되었는가? {}".format( chord_task.ready() ) )