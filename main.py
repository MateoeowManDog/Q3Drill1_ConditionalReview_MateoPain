from pyscript import document
#the funtion of the code, this is to find the average of two scores
def find_average(event=None):
    s1 = int(document.getElementById("score1").value or 0)
    s2 = int(document.getElementById("score2").value or 0)

    avg = (s1 + s2) / 2 #this is how the code computes the average
    if avg >= 75:
     msg =f"Average: {avg:.2f} Passed? yes!✅ " 

    else:
        msg = f"Average: {avg:.2f} Failed? yes!❌ "

    document.getElementById("result").innerHTML = msg
