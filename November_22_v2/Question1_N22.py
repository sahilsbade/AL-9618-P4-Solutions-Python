Jobs = []
NumberOfJobs = None


def Initialise():
    global Jobs
    global NumberOfJobs

    Jobs = [[-1, -1] for x in range(0, 100)]
    NumberOfJobs = 0


def AddJob(JobNumber, Priority):
    global Jobs
    global NumberOfJobs

    if NumberOfJobs == 100:
        print("Job not added")

    else:
        Jobs[NumberOfJobs] = [JobNumber, Priority]
        NumberOfJobs += 1
        print("Added")


Initialise()

AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)


def InsertionSort():
    global Jobs
    global NumberOfJobs

    for x in range(1, NumberOfJobs):
        Current1 = Jobs[x][0]
        Current2 = Jobs[x][1]
        counter = x
        while counter > 0 and Jobs[counter - 1][1] > Current2:
            Jobs[counter][0] = Jobs[counter - 1][0]
            Jobs[counter][1] = Jobs[counter - 1][1]
            counter = counter - 1

        Jobs[counter][0] = Current1
        Jobs[counter][1] = Current2


def PrintArray():
    global NumberOfJobs
    global Jobs

    for x in range(0, NumberOfJobs):
        print(f"{Jobs[x][0]} priority {Jobs[x][1]}")


InsertionSort()
PrintArray()
