#!/bin/bash

LOGFILE="monitor_pid_log.txt"

declare -A SCREENS
SCREENS["gen"]="/root/rl-swarm/run_rl_swarm.sh"


declare -A PIDFILES
PIDFILES["gen"]="/tmp/gen_swarm.pid"


while true; do
    for screen in "${!SCREENS[@]}"; do
        script_path="${SCREENS[$screen]}"
        pid_file="${PIDFILES[$screen]}"

        if [ -f "$pid_file" ]; then
            swarm_pid=$(cat "$pid_file")

            if ps -p "$swarm_pid" > /dev/null 2>&1; then
                echo "[$(date)] [$screen] PID $swarm_pid is running." | tee -a "$LOGFILE"
            else
                echo "[$(date)] [$screen] PID $swarm_pid is NOT running. Restarting..." | tee -a "$LOGFILE"
                screen -S "$screen" -X stuff $"bash $script_path\n"
            fi
        else
            echo "[$(date)] [$screen] PID file $pid_file not found. Restarting..." | tee -a "$LOGFILE"
            screen -S "$screen" -X stuff $"bash $script_path\n"
        fi
    done

    sleep 30
done
