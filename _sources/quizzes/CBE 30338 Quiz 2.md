



Name (please print clearly): ______________________________________________________________________

# CBE 30338: Quiz 2 (40 pts)

Chemical Process Control

April 4, 2023



* This is a closed-book, no electronics exam. You are allowed a pencil/pen and one page of notes (8.5 x 11-inch paper, both sides, personally handwritten, no copies). Turn your notes in with the quiz.
* You may take the pages apart but then print your name at the top of every page.
* Show your work on the quiz paper. Indicate your answer by enclosing it in a box. Always show relevant units.

<div style="page-break-after: always; break-after: page;"></div>

---

|           |      |
| :-------- | ---- |
| Problem 1 | /10  |
| Problem 2 | /20  |
| Problem 3 | /10  |
|           |      |
| TOTAL     | /40  |

<div style="page-break-after: always; break-after: page;"></div>
## Problem 1 (10 pts)

The following diagram shows a heat exchanger and accompanying control hardware. The system is initially at steady state under manual control. **Note: The controller output denoted "CO" in the diagram corresponds to the manipulated variable "MV" that we use in class.**

![](/Users/jeff/Google Drive/GitHub/cbe30338-book/quizzes/heatexchangebig.jpg)



The operator conducts a step test on this unit where "CO" is changed from 39% to 42%. The results are: 

![](/Users/jeff/Google Drive/GitHub/cbe30338-book/quizzes/hesteptestbig.png)

Estimate values for the following quantities (including units). Annotate the chart to show how the two time constants are related to the step test.

1. [3 pts] Sketch your work on the chart above.





2. [3 pts] What is the steady-state gain $K$ ?





3. [2 pts] What is the first-order time constant $\tau$ ?





4. [2 pts] What is the time delay $\theta$ ?











<div style="page-break-after: always; break-after: page;"></div>

## Problem 2 (20 pts)

The following code has been used to create instances of PI control in a large chemical plant. Assume both $K_p$ and $K_I$ are non-zero unless stated otherwise.

```
def Proprietary_Control(Kp, Ki, MV_bar=0, MV_min=0, MV_max=100):
    MV = MV_bar
    PV_prev = None
    while True:
        t_step, SP, PV, MV = yield MV 
        e = PV - SP
        if PV_prev is not None:
            MV = MV - Kp*(PV - PV_prev) - t_step*Ki*e 
            MV = max(MV_min, min(MV_max, MV))
        PV_prev = PV
    
```

1) [2 pts] Is this a P, PI, or PID control?







2) [2 pts] Will this controller exhibit steady-state offset?  Why or why not? (Explain why using the equations embedded in the code above.)







3) [2 pts] Suppose there is a sudden change in setpoint SP. Will that cause a sudden change in the manipulated variable MV?  Why or why not?







4. [2 pts] Will this controller exhibit anti-reset windup? Why or why not?







5. [2 pts] Locate the yield statement.  Why does MV appear on both sides of the equality symbol?







6. [2 pts] Locate the first statement where MV is updated. Why does MV appear on both sides of the equality symbol? 





7. [2 pts] Is this in velocity or position form?







8. [2 pts] Suppose the operator sets $K_I = 0$. How will the manipulated variable respond if the setpoint SP changes?





9. [4 pts] Write a generator for a proportional-only controller using the code above as a starting point. The proportional control should be in velocity form, and should respond to set point changes.

<div style="page-break-after: always; break-after: page;"></div>

## Problem 3 (10 pts)

The following chart shows a grid of candidate tunings for PI control. The proportional control gain $K_p$  (called $K_c$ in the chart) is changed along the vertical axis, and the integral time constant $\tau_I$ along the horizontal axis. (In our nomenclature, $K_I = K_p/\tau_I$). The chart shows the response of the closed-loop system to a step change in a disturbance.

![](/Users/jeff/Google Drive/GitHub/cbe30338-book/quizzes/tuning.png)



1. [2 pts] Are there any unstable responses?  If so, which one(s)?  (Note the number in the upper right corner of each sub-chart).





2. [3 pts] In chart #3 (upper right), is the integral gain too high or too low?  Explain what you see.





3. [3 pts] Which of these tunings would you recommend for industrial use?





4. [2 pts] The Ziegler-Nichols rules for PI tuning are $K_p = \frac{0.9\tau}{K\theta}$ and $K_I = \frac{0.3\tau}{K\theta^2}$  where $K$ is the gain measured in a step test, where $\tau$ is the time constant, and $\theta$ is the dead time.  In this chart, $K_P = K_c$ and $K_I = K_c/\tau_I$. Suppose $\tau_I = 12$ minutes provides a satisfactory tuning, then estimate the dead time in the process.







