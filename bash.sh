# GPIO Pins - Bash
# Written by Asha Gupta

gpio mode 0 out #setting the output pins
gpio mode 2 out

for (( x=0; x<=9; x++ ))  #loop that runs twice
  do  
  gpio write 0 1  #turn the leds on
  gpio write 2 1
  sleep 1         #wait one second
  gpio write 0 0  #turn them off
  gpio write 2 0
  sleep 1         #wait one second

done              #code finishes

