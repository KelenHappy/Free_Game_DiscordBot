#!/bin/bash
run_task(){
  source venv/bin/activate
  export BOT_TOKEN=Your Token
  python3 main.py
}
while true; do
  run_task()
  sleep 60
done
