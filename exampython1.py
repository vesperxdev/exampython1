x = 3
curstudents = 3
binary = bin(x)
hexval = hex(x)
octal = oct(x)
school = 'OS-SCi'
active = True
print('OS-Sci is a school with' + ' ', curstudents, 'students. \nIn other literals, that is :' + ' ', binary, hex, octal)
students = []
studentrecord = ()
allgrades = {}

'''lists, strings, binaries, booleans, printing, dictionaries, integers etc., covering most of the topics in the 
first few lectures to ensure that all the topics covered by the PCEP'''


def grades(name, scores):
    return {name: list(scores)} #defining what the grades function will cover

def average(scores):
    total = 0
    for score in scores:
        total += score
    return total/len(scores) #pretty basic average, where a score just gets a loop based on a +1 on the score

def gradename(avg):
    if avg >= 90 and avg <= 100:
        return 'Excellent'
    if avg >= 80 and avg <= 89:
        return 'Good'
    if avg >= 70 and avg <= 79:
        return 'Above Average'
    if avg >= 55 and avg <= 69:
        return 'Pass'
    elif avg >= 40 and avg <= 54:
        return 'Fail, but recoverable for next time'
    else:
        return 'Hard Fail'

'''Defining what the grade would be, initially I wanted to do the Dutch versions of 'goed', 'ruim voldoende', 'voldoende' etc., however
it wouldn't be universal whereas English is a universal language '''

def validscores(value):
        try:
            score = float(value)
            if not (0 <= score <= 100):
                raise ValueError('Invalid score (out of range)')
        except ValueError:
            raise ValueError('Not a valid score')
        else:
            return score
        finally:
            pass

'''defining the errors with a try loop, defining an exception and raising a ValueError with a finally function'''

def addstudent(name, scores):
    students.append(name)
    allgrades[name] = scores
    global studentrecord
    studentrecord = tuple(students)

'''appending, recalling global, and getting the last functions together to get the grademanager going'''

def grademanager():
    print(school + ' ' + 'Grade Manager for OS-SCi Exam')
    count = 0
    while count < curstudents:
        name = input('Enter student name (or "none" to end program): ').strip()
        if name == "none":
            break
        rscores = input('Enter scores (by commas separated): ')
        scores = []
        for pscore in rscores.split(','):
            pscore = pscore.strip()
            try:
                scores.append(validscores(int(pscore)))
            except ValueError as te:
                print('Skipped an invalid score', repr(te))
        if scores:
            addstudent(name, scores)
            count += 1
        else:
            print(f'No scores entered for {name} discarded.\n')

    print('Grade Record of', school)
    for name in students:
        scores = allgrades[name]
        avg = average(scores)
        grade = gradename(avg)
        print(name, '', avg, '', grade)
    print(f'\nCurrent Record (tuple): {studentrecord}')
    print(f'Total students graded: {len(students)}')

'''creating the tool, printing what the tool is and having the count set up to lead to a +1 loop while simultaneously 
ensuring that the input is sorted accordingly by using commas after inputting the rscore (raw scores) into pscores (precise scores)
and ensuring there's an output when there is a value error. Afterwards it prints accordingly with the errors presented and the scores that the 
students gathered. I was debating creating a dictionary where it keeps appending more and more to a unique name, but I feel like that'd be
going too advanced. Maybe for the next time.'''
grademanager()