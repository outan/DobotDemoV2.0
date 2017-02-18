import sys,threading,time
import DobotDllType as dType

api = dType.load()

def GetPoseTask():
    pos = dType.GetPose(api)
    threading.Timer(0.2, GetPoseTask).start()

threading.Timer(0.5, GetPoseTask).start()

errorString = [
    'Success',
    'NotFound',
    'Occupied']

result = dType.ConnectDobot(api, "", 115200)
print("Connect status:",errorString[result[0]])

if (result[0] == 0):
    # Set command timeout
    dType.SetCmdTimeout(api, 3000)

    dType.SetJOGJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200)
    dType.SetJOGCoordinateParams(api, 200, 200, 200, 200, 200, 200, 200, 200)
    dType.SetJOGCommonParams(api, 100, 100)

    while 1:
        dType.SetJOGCmd(api, 1, 1)
        time.sleep(0.2)
        dType.SetJOGCmd(api, 1, 0)
        time.sleep(1)
        dType.SetJOGCmd(api, 1, 2)
        time.sleep(0.2)
        dType.SetJOGCmd(api, 1, 0)
        time.sleep(1)
    dll.DisconnectDobot()
