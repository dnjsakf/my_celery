# run_chain.py
from tasks import calc
from celery import group

tasks = [ calc.add.s( i, i+1 ) for i in range(1, 5) ]

grouping = group( tasks )
group_task = grouping() # 또는 grouping.apply_async()
 
print( "\n# 1. Task 확인" )
print( "tasks = {}".format( tasks ) )
print( "group_task.id = {}".format( group_task.id ) )
print( "group_task.type = {}".format( type(group_task) ) )
 
print( "\n# 2. Task 상태 확인" )
print( "Subtask가 모두 준비되었는가? {}".format( group_task.ready() ) )
 
print( "\n# 3. 실행결과 확인" )
print( "몇건이 완료 되었는가? {}".format( group_task.completed_count() ) )
print( "완료된 결과를 반환. {}".format( group_task.get() ) )
print( "호출한 순서대로 반환. {}".format( group_task.join() ) )
print( "몇건이 완료 되었는가? {}".format( group_task.completed_count() ) )
 
print( "\n# 4. Task 상태 확인" )
print( "Subtask가 모두 준비되었는가? {}".format( group_task.ready() ) )
print( "모두 성공했는가? {}".format( group_task.successful() ) )
print( "실패가 있는가? {}".format( group_task.failed() ) )