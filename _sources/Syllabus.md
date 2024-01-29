# Syllabus

## CBE 30338 Description

**CBE 30338 Data Analytics, Optimization, and Control** introduces students to the analysis and design of control systems for chemical and biochemical processes. Applications include chemical and biological reactors, separation processes, autonomous biomedical devices, and examples from other engineering disciplines. 

The major topics of the course are

* Modeling and Parameter Estimation
* Feedback Control
* Process Data Analytics
* Optimization
* Predictive Control

Python and hands-on control experiments are integrated into the course. 

The lab sessions (CBE 32338) provide opportunities for hands-on coding and experimentation using the [Temperature Control Laboratory](./tclab/00.00-tclab.md). In leu of a textbook, students should purchase their own device from [Amazon](https://www.amazon.com/TCLab-Temperature-Control-Lab/dp/B07GMFWMRY) or [apmonitor.com](https://apmonitor.com/pdc/index.php/Main/PurchaseLabKit). 

## Learning Objectives

Students completing this course will be able to:

* Identify process models and fit the models to data
* Design and implement feedback (e.g., advanced PID) control
* Manipulate time series data and extract process information
* Create and solve steady-state optimization models
* Apply the principles of modeling and control to novel applications

## Course Information

**Canvas link:** [SP24-CBE-30338-01 Data Analytics, Optimization, and Control](https://canvas.nd.edu/courses/82955)

**Dates:** January 16 - April 30, 2024

**Class:** CBE 30338 Tuesday and  Thursdays, 9:15 - 10:45 am, DeBartolo 136

**Lab/Tutorial:**  You must be registered for one of these lab/tutorial sections.
* CBE 32338-01 Friday, 11:35 am - 12:25 pm, Fitzpatrick A68
* CBE 32338-02 Friday, 12:50 am - 1:40 pm, Fitzpatrick A68

Seating in A68 is limited. Pleae attend the lab session for which you are registered.

**Prerequisites:** This course assumes knowledge of modeling and analysis with differential equations, procedural programming in Python, mass and energy balances. Students taking this course will normally have completed

* CBE 20258 Numerical and Statistical Analysis
* MATH 20580 Linear Algebra and Differential Equations (or ACMS equivalent)
* MATH 30650 Differential Equations (or ACMS equivalent)

Students without this background should contact the instructor before registering for the course.

**Required Materials:** The following materials should be acquired at the start of the course.
1. [Temperature Control Lab kit](http://apmonitor.com/pdc/index.php/Main/ArduinoTemperatureControl) is an Arduino based device used in this course as a "hands-on" laboratory for learning the principles and implementation of process control. It is available by on-line order from [Amazon](https://www.amazon.com/TCLab-Temperature-Control-Lab/dp/B07GMFWMRY) or [Apmonitor.com](https://apmonitor.com/pdc/index.php/Main/PurchaseLabKit) for about $40  USD.
2. A laptop/desktop computer with USB-A port, or a USB-C port and a USB-C to USB-A converter.
3. An up-to-date installation of the [Anaconda Individual Edition](https://www.anaconda.com/products/individual)  for Python programming. **Follow the instructions [here](https://appdividend.com/2020/05/12/how-to-update-anaconda-upgrade-anaconda-navigator/) to update an older installation.**

## Instructor and Teaching Assistants

```{list-table}
:header-rows: 1
:widths: 20 20 20 20 20

* - [Prof. Alex Dowling](https://dowlinglab.nd.edu/people/professor-alexander-w-dowling/)
  - [Maddie Watson](https://dowlinglab.nd.edu/people/madelynn-watson/)
  - [Hailey Lynch](https://dowlinglab.nd.edu/people/hailey-lynch/)
  - [Molly Dougher](https://dowlinglab.nd.edu/people/molly-dougher/)
  - [Zhicheng Lu](https://dowlinglab.nd.edu/people/zhicheng-lu/)
* - ![](https://dowlinglab.nd.edu/assets/320333/200x200/dowling_alex_sq.jpg)
  - ![](https://dowlinglab.nd.edu/assets/477606/200x200/senior_composite.png)
  - ![](https://dowlinglab.nd.edu/assets/497694/200x200/img_3436.jpg)
  - ![](https://dowlinglab.nd.edu/assets/496713/200x200/img_2112_3.jpeg)
  - ![](https://dowlinglab.nd.edu/assets/552006/200x200/zhicheng.jpg)
* - Primary Instructor
  - Lead TA
  - Senior TA
  - Senior TA
  - TA
* - Wednesdays, 2 - 3pm, 369 NSH
  - Thursdays, 2 - 3pm, 252 NSH $^\dagger$
  - (same)
  - (same)
  - (same)
```
Office hours are lists in the last row. TAs share office hours. $^\dagger$ TA office hours will be held in 366 NSH on March 28, 2023. 

## Discussion Board (Canvas) and Email Correspondance

* Post your questions to the **discussion board in Canvas**
* Instructor only: adowling@nd.edu, ''CBE 30338'' in the subject, private official matters (e.g., excused absence, testing accommodations)

We encourage you to post all your questions, including your mathematical models, pseudocode, and code screenshots, to the public **discussion board in Canvas**. We are doing this for a few reasons:
1. As professionals, you'll need to be comfortable asking questions in front of a team. We want to cultivate a positive and friendly learning environment where everyone can practice this skill during the semester.
2. By answering questions in the public discussion board, everyone in the class can access the same information.
3. We would like to cultivate a learning community with peer instruction; as professionals, you must answer your peers' questions.
4. Many scientific software have online discussion boards to ask technical questions and report bugs. Using the **discussion board in Canvas** will help you develop comfort in asking questions this way.

## Required Materials

Required notes and materials for the course are available at the Github/web repositories 

* [ndcbe/controls](https://ndcbe.github.io/controls/Readme.html) 
* [jckantor/TCLab](https://github.com/jckantor/TCLab)

Additional material will be taken from:

* Åström, Karl Johan, and Richard M. Murray. Feedback systems: an introduction for scientists and engineers.  Second Edition (Version v3.1.5 dated 2020-07-24). Princeton University Press. 
* Douglas, Brian. [The Fundamentals of Control Theory]([https://drive.google.com/file/d/1LAjaDDViFG4H7dQ6PQVHo8XSQHS59GJf/view]. See [https://engineeringmedia.com/](https://engineeringmedia.com/) for links to video.

This textbook is available for download from the website (preferred, latest edition with corrections) and Hesburgh Library at https://ebookcentral.proquest.com/lib/ndlib-ebooks/detail.action?docID=475844. 

Additional supplementary materials related to process control will be distributed from time-to-time during the course.

* [Introduction to Python for Science](https://physics.nyu.edu/pine/pymanual/html/pymanMaster.html)
* [BYU Process Dynamics and Control course website](http://apmonitor.com/pdc/index.php/Main/HomePage)
* [Resourcium](https://resourcium.org/)

## Assessment and Grades

Grades for CBE 30338 and CBE 32338 are consolidated into a single grade assigned to CBE 30338. There is no separate grade or credit assigned for CBE 32338.

Grades are based on a weighted assessment of performance in the following categories:

* Class Participation and Professionalism: 5\%
* Assignments: 45\%
* Exam: 25\%
* Group Project: 25\%

### Class Participation and Professionalism 

You are expected to attend and actively participate in all class sessions.  If you miss class for an official University excused function, please find notes for that lecture, do the  reading, and avail yourself of office hours to catch up on the missed material.

Class sessions will include opportunities to respond to instructor questions and other active learning exercises. All interactions will be civil, respectful, and inclusive. If you have any concerns about classroom dynamics, please feel free to speak with the instructor.

At the end of the semester, the instructor will assign grades for class participation and professionalism at their discretion. Students who are good class citizens, i.e., actively engage in class and lab activities, work well with peers, and ask and answer questions on the Canvas discussion board, will receive full marks. In contrast, the following may result in a reduced grade:
- Unprofessional behavior toward peers, instructors, teaching assistants, or others in the campus community. (This may also result in other disciplinary action per university policies.)
- Repeatedly sending emails to the instructor or TAs on topics that should be addressed in the Canvas Discussion board (e.g., assignment help, class policy questions).
- Repeatdely sending emails without "CBE 30338" in the subject.
- Not actively participating in class or lab activities.
- Missing significant numbers of class sessions without an excuse recognized by the university.
- Arriving late to class as this causes a distrubtion.


### Assignments

Homework and labratory assignments are critical to developing the skills needed to succeed in the course and in the major. Accordingly, assignments are a required element of the course. Missing assignments will be scored as zero. Three or more missed assignments will result in an incomplete for the course. Group study is encouraged, but the submitted work must be your own. Students must be able to explain all of their submitted work.

Please see our [semester schedule](./Schedule.md) for a listing of assignments and deadlines.

### Exam

There will be one in-class exam on Thursday, April 4. The exam will be open book but without access to a computer or the internet. Students who take notes on a tablet should sit in the front rows during the exam and will be monitored by the teaching team. Tablets may only be used to access your notes, i.e., internet and other connectivity must be disabled.

### Final Project

The final project for CBE 30338 is in-depth exploration of a dynamic modeling, optimization, or control problem of your choice. You will work in groups (at least three, no more than four, no exceptions), select a problem of interest, and develop an analysis or control design using the skills you learned in this course.  The essential elements of the project are:

* **Preliminary reports** consisting of a problem statement, a meeting with the instructor to review the project, and a progress report.

* A **Group presentation** to the class.

* A **Final Report** that includes at least one executable demonstration of your project. The executable element might consist of a Python/Jupyter notebook, a simulation prepared in an industry standard format, or video of experiment or hardware demonstration.

### Grading Standards

All computer code must be commented. No exceptions.

All graphs must have labeled axes with UNITS. Likewise, all final answers need UNITS and should be rounded to the appropriate number of significant digits.

Be sure to answer the questions asked in the assignment. When discussing results, only report the appropriate number of significant figures.

**Formatting**: Your submission should include neatly written code with extensive comments, well-labeled graphs, and answers to any discussion questions. Your project submissions should be professionally formatted, like a laboratory report. Your response to discussion questions and code comments MUST be written in your own words. Please see [coding standards](https://ndcbe.github.io/data-and-computing/notebooks/01/Pseudocode.html#python-and-commenting-guidelines).

**Project:** This will be graded in-depth (unlike the homework). Be sure to triple check the Python code and plotting formatting standards. We expect [publication-quality plots](https://ndcbe.github.io/data-and-computing/notebooks/01/Publication-Quality-Figures.html) for this project.

**Pseudocode:** You should get in the habit of first writing pseudocode when starting assignments or projects. Some assignments may require you to turn in pseudocode. In this case, your pseudocode needs to reflect all your solution's main steps and logic. You do not need to rewrite your pseudocode if your final solution has different main steps or logic. Instead, you should update your pseudocode with a few notes showing the change. Rewriting the pseudocode is helpful if you find a logical mistake but get stuck making modifications. Prof. Dowling has been programming in Python for 20 years. He writes pseudocode, and so do other professional software developers. Expect one of the first questions in office hours to be, "can we look at your pseudocode together?".

### Regrade Requests

We will undoubtedly make some mistakes during grading. Regrades to correct these mistakes will be considered for **up to ONE week after assignment grades are posted online**. 

Submit your regrade requests in writing via Gradescope. Please include a 1-3 sentence explanation of the grading mistake. We will not consider adjustments to the grading point distribution.

All regrade requests will result in a reevaluation of the entire assignment. For rubric selection mistakes in Gradescope, we will recheck all rubric selections. For more substantial regrade requests, the grader may reexamine the whole problem (including all subparts) and possibly the entire assignment.

### Late Policy

The following policy will apply to all assignments (homework, projects, etc.):
* Up to 1 hour late: grace period with no penalty
* 1 hour to 24 hours late: 10% penalty of total available points
* 24 to 48 hours late: 20% penalty of total available points
* 48 to 72 hours: 30% penalty of total available points
* Beyond 72 hours: assignment not accepted

If there is an extenuating circumstance, please email the instructor with ``CBE 30338'' in the subject. Please send your requests for extensions at least 24 hours before the deadline (unless your specific circumstance prevents this). Please briefly explain the extenuating circumstance when requesting an extension and propose an alternate deadline.

## Honor Code

*As a guiding principle, if you are not comfortable explaining your solution strategy to an instructor or TA, you should not turn in the work as your own.*


### Collaboration Policy

You are permitted (and encouraged) to discuss solution approaches to the weekly homework assignments with classmates. However, there must be no wholesale copying or paraphrasing of code, solutions, or written discussions. You are strongly encouraged to ask questions, including posting pseudocode or code screenshots, on the discussion board on Canvas. Likewise, you may use any material posted by the instructors or your classmates in the discussion board on Canvas that you understand. Copying code from classmates or the discussion board, you do not understand is prohibited. This policy facilitates collaboration while ensuring everyone in the class has the same access. Students MAY NOT use old files and solutions for the homework assignments: you must do the problems for homework to be able to do them on the exams too.

Your work may be electronically tested for plagiarized content. For example, Gradescope can detect highly similar code (i.e., plagiarism for computer code) while distinguishing from provided templates. Plagiarism is a serious offense and will have severe consequences per University, College, and Department procedures.

To remove ambiguity, the following is a non-exhaustive list of collaborative scenarios that are **PERMITTED** under the above policies:
* You work with a group of classmates to write pseudocode together. Each group member participates at least once (e.g., asks a question). One person in the group takes a picture and emails it to everyone. Then each person rewrites the pseudocode on their own for the homework submission. You rewrite the comments in your own words (to be more evident). You also decide to replace a `while` loop with a `for` loop. The collaboration policy permits this because the work is your own. You made a clear intellectual contribution.
* You are working on a homework assignment and get stuck on an error message. After consulting the class notes and Google for 5 minutes, you post a screenshot of your code and the error message to Canvas. A classmate posts some alternate code that fixes your error. You replied by thanking the student and asking for clarification on why the alternate code works and your approach was wrong. Your post leads to a good discussion, with the instructor explaining a concept and clearing up your confusion. The solution you turn in includes the changes suggested by your classmates. The collaboration policy permits this because you are comfortable explaining your solution strategy, including why the proposed modification was necessary to fix the error.
* You are working on the homework assignment closer to the deadline than you would like to admit. You get stuck on an error message but quickly find a discussion thread on Canvas. You read through the suggestions from your classmates and the instructor. The post answers your significant questions, and the proposed fix works! You adopt it into your code and add a comment acknowledging your classmates on Canvas for help. You still have a minor question about if there is an alternate way to solve the problem, so you post on Canvas and continue with the assignment. The collaboration policy permits this because you made a good faith effort to understand the proposed solution. Even though you have an outstanding minor doubt, you sought help from the TAs, instructor, and classmates. You also acknowledged the source (Canvas discussion) for the code you used and thus are not presenting it as your own.  

The following is a non-exhaustive list of collaborative scenarios that are **PROHIBITED** under the above policies:
* You are working on your homework alone in the library, but two tables away, there is a group of your classmates. They work through the pseudocode on a whiteboard and do not erase it after leaving. You take a picture “just in case”. You later get stuck and frustrated. You end up copying line by line most of their pseudocode and turn this in. You have some doubts about the approach but ran out of time. The collaboration policy prohibits this because the work is not your own. Moreover, you would be unable to explain your solution approach to the TA or instructor confidently.
* It is late at night, you are frustrated with syntax errors, and you cannot get one of the homework problems to work. You find a screenshot on Canvas of code from a classmate and an associated discussion. Desperate to finish the assignment, you adapt your code to follow the screenshot. To keep it simple, you copy line-by-line, do not change variable names, and copy some comments but skip others. You end up submitting code that looks almost identical to your classmate. You remember the instructor keeps emphasizing the comments should be in our own words to show that you understand the solution. You decide to go to bed and add those comments in the morning. You oversleep and submit the code without any comments or acknowledgments from your classmates. The collaboration policy prohibits this because you submitted work that is not your own. You should have acknowledged sources, and you can not confidently explain the solution procedure to the instructor or TA.
* You have no prior programming experience before college and feel like you are falling behind. You suspect the homework takes you three times as long as your classmates. You conclude the only way you can keep up is to do the homework with a partner. They do half the assignment, and you do the other half. You then exchange solutions. The person who completes each problem then explains the answer to the partner. Each person changes the comments, adds some extra white spaces, and changes a few variable names to ensure the solutions are not identical. The collaboration policy prohibits this because each person did not make an honest effort to solve every problem on their own. Although each person either explained or had the solutions presented to them, they likely need help to defend all of their solutions to the TA or instructor. 

### Artificial Intelligence Policy

Please review the university-wide [Generative AI Policy for Students](https://honorcode.nd.edu/generative-ai-policy-for-students-august-2023/) distributed via email in August 2023. We will adopt the following additional policies for CBE 30338:
* Anyone who uses Generative AI tools (e.g., Copilot, ChatCPT) must add a discloser statement at the end of their assignment submissions. In this disclosure statement, you must describe which Generative AI tool you used and how you used it. For example, many professional scientists and engineers find these technologies especially helpful for refining the quality of plots generated in Python.
* Many practicing scientists and engineers find [Copilot](https://copilot.microsoft.com/), which is available in [Visual Studio Code](https://visualstudio.microsoft.com/github-copilot/, more helpful and reliable than [ChatGPT](https://chat.openai.com). However, ChatGPT and Copilot occasionally generate code with incorrect logic or calculations. You should critically examine any code from Generative AI tools, collaborators, and class examples.
* As described above, you must comment all code in your assignments. Furthermore, students must write comments in their own words. This ensures that anyone who uses Generative AI for help still practices interpreting the code. In other words, everyone who passes CBE 30338 should be able to perform calculations and explain the underlying logic in code.
* Students are expected to use descriptive variable names; sometimes, Generative AI tools suggest generic variable names.
* Students are responsible for understanding all code they submit, especially if they collaborate with another student or use Generative AI. The class exam will be individual and without access to Generative AI tools.
* Answers to discussion questions, which often critically interpret results or connect calculations with concepts from class, must be written in your own words. You should use tools like [Grammarly](https://www.grammarly.com) to improve spelling, grammar, sentence structure, and conciseness. But you must perform the critical analysis on your own.

## Inclusiveness, Mental Health, and Disabilities

The University of Notre Dame is committed to social justice. We share that commitment and strive to maintain a positive learning environment based on open communication, mutual respect, and non-discrimination. In this class, we will not discriminate on the basis of race, sex, age, economic class, disability, veteran status, religion, sexual orientation, color, or national origin. Any suggestions as to how to further such a positive and open environment will be appreciated and given serious consideration.

Diminished mental health can interfere with optimal academic performance. The source of symptoms might be related to your coursework; if so, please speak with us. However, problems with other parts of your life can also decrease academic performance. The University Counseling Center (UCC) provides cost-free and confidential mental health services to help you manage personal challenges threatening your emotional or academic well-being. Remember, getting help is a smart and courageous thing to do — for yourself and for those who care about you. For more resources, please see ucc.nd.edu. The UCC is located on the third floor of Saint Liam Hall Phone: 574-631-7336. Hours: Monday-Friday 8:30am – 5:00pm. Urgent Crisis Line 24/7. 

Any student who has a documented disability and is registered with Disability Services should speak with the professor as soon as possible regarding accommodations. Students who are not registered should contact the [Office of Disability Services](https://sarabeadisabilityservices.nd.edu/). 
