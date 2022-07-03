# APIs' Tasks

http://127.0.0.1:8000/task_one/


http://127.0.0.1:8000/task_two/



- Please Check photos (TASK_ONE, TASK_TWO).png 
  
---------------------------
Feel free to use default python venv like myself or any other one.
Activate the virtual env
```
pip install -r requirements.txt
```
Free port 8000 if needed(UNIX BASED).
```
sudo lsof -t -i tcp:8000 | xargs kill -9
```
Run {migrate} & {makemigrations} then {createsuperuser}.
in case of problems with migrations, plz makemigrations & migrate the accounts app first then migrate the rest. or try to use --run-syncdb with migrate in worst case.


