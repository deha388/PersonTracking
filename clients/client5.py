import paho.mqtt.client as mqtt
import time

global list
HashTable = [[] for _ in range(4000)]
HashTable1 = [[] for _ in range(4000)]
global keyMapDict
keyMapDict={}

def closest_value(value, iterable):
    storage = []
    for i in iterable:
        storage.append((abs(value - i), i))
    result = min(storage)
    index = iterable.index(result[1])
    try:
        meanValue = iterable[index - 3]
        # + iterable[index - 1] + iterable[index] + iterable[index + 1] + iterable[index + 2]
        keyValue = meanValue

    except IndexError:
        keyValue = value

    return keyValue


def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


# Function to display hashtable
def display_hash(hashTable):
    for i in range(len(hashTable)):
        if len(hashTable[i]) > 0:
            print(i, end=" ")
        else:
            pass

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

    print()
    # Creating Hashtable as

# a nested list.

# Hashing Function to return
# key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)


# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


def findKey(hashTable):
    for i in range(len(hashTable)):
        if len(hashTable[i]) > 0:
            avarageValue = sum(hashTable[i]) / len(hashTable[i])
            # print(i, end=" " + "----")
        else:
            pass

        for j in hashTable[i]:
            # print("-->", end=" ")
            # print(j, end=" ")

            #find to avarege number for the middle point of list

            # print(avarageValue)

            #closest number function

            k = closest(hashTable[i], avarageValue)
            #taking index to closest number is helping us the keyValue so keyValue==(i+(i+1)+(i+2)+(i-1)+(i-2))==RSSI
            index = hashTable[i].index(k)

            #flowing value need to sort for the real RSSI
            hashTable[i].sort()

            try:
                if len(hashTable[i]) <= 5:
                    keyValue = avarageValue
                else:

                    if hashTable[i][index] == hashTable[i][index + 1] == hashTable[i][index + 2] == hashTable[i][index + 3] == hashTable[i][index + 4]:

                        keyValue = hashTable[i][index]

                        break


                    elif hashTable[i][index] == hashTable[i][index + 1] == hashTable[i][index + 2]:

                        meanValue = hashTable[i][index + 3] + hashTable[i][index - 1] + hashTable[i][index] + \
                                    hashTable[i][index + 1] + hashTable[i][index + 2]
                        keyValue = meanValue / 5


                    else:

                        meanValue = hashTable[i][index - 2] + hashTable[i][index - 1] + hashTable[i][index] + \
                                    hashTable[i][index + 1] + hashTable[i][index + 2]
                        keyValue = meanValue / 5



            except IndexError:
                keyValue = avarageValue


            # print(keyValue)

            insert(HashTable1,i,keyValue)

    # print()

##########Defining all call back functions###################


def on_connect(client, userdata, flags, rc):  # called when the broker responds to our connection request
    print("Connected Client1 - rc:", rc)

def on_message(client, userdata,
               message):  # Called when a message has been received on a topic that the client has subscirbed to.

    if str(message.topic) != pubtop:

        msg = message.payload

        if len((message.payload)) == 8:

            # Consantrator wants to know,anyone listening to him or not
            # so sending 8 byte controllerMessage
            # responseMessage include Datetime,Checksum and etc totally 13 bytes data sending to Consantrator in byte format

            list = [0x01, 0x00, 0x09, 0xEF, 0x02, 0x01, 0x07, 0xE1, 0x16, 0x16, 0x16, 0x25, 0x04]
            # hexa value to byte type convert
            byte = bytearray(list)
            # publish the message to topic
            client.publish(pubtop, byte)
        else:
            # print(msg)
            # after starting taking messagePacket need to "understand data"
            # converting data to Hex format
            value = bytearray(msg)
            HexList = []
            HexList.append(value.hex('-'))
            data = HexList[0]

            # formatting data to splitting
            asd = []
            asd = data.split('-')

            # Data include useless data like id,date,time --getting rid of them
            for i in range(4):
                asd.pop(0)

            for i in range(9):
                asd.pop(-1)

            # print(asd)

            global arrs
            arrs = []

            # data splitting into groups of six
            def split(arr, size):
                while len(arr) >= size:
                    pice = arr[:size]
                    arrs.append(pice)
                    arr = arr[size:]
                arrs.extend(arr)

            split(asd, 6)
            # after splitting to 6 pieces ,every groups of data first two elements givee us the id
            # vereinigung der Data
            global newList
            newList = []
            length = len(arrs)
            for i in range(length):
                arrs[i][0: 2] = [''.join(arrs[i][0: 2])]
                arrs[i].pop(1)
                for j in range(2):
                    arrs[i].pop(-1)
                # newList.append(arrs[i])
                # print(newList)
                # print(arrs)
                # pice[0: 1] = [''.join(pice[0: 1])]
            # print(arrs)

            # hex value to integer
            for i in range(length):
                arrs[i][0] = int(arrs[i][0], 16)
                arrs[i][1] = int(arrs[i][1], 16)
                insert(HashTable, arrs[i][0], arrs[i][1])
                # print(arrs[i])
            print(arrs)
            findKey(HashTable)

            # List=["asd","asd","asd"]
            # with open("value.txt", 'a') as output:
            #     for item in List:
            #         output.write("Message"+":" + str(item)+"/n")

            # saving data to in a txt file
            with open("../value.txt", 'a') as output:
                for item in arrs:
                    output.write("Message" + ":" + str(item) + "\n")


def on_subscribe(client, userdata, mid, granted_qos):  ##Called when the broker responds to a subscribe request.
    print("Subscribed:", str(mid), str(granted_qos))


def on_unsubscirbe(client, userdata, mid):  # Called when broker responds to an unsubscribe request.
    print("Unsubscribed:", str(mid))


def on_disconnect(client, userdata, rc):  # called when the client disconnects from the broker
    if rc != 0:
        print("Unexpected Disconnection")


subtop = "+/+/TA0000410/#"
pubtop = "BTtakip/Pavofwu/TA0000410/cmd"

broker_address = "localhost"
port = 1883

def runClient5():
    client = mqtt.Client()
    client.on_subscribe = on_subscribe
    client.on_unsubscribe = on_unsubscirbe
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, port)
    time.sleep(1)

    FLAG = True
    chat = None

    client.subscribe(subtop)
    client.loop_start()

    time.sleep(120)

    client.disconnect()
    client.loop_stop()

    for i in range(len(HashTable1)):

        for j in HashTable1[i]:
            keyMapDict[i] = HashTable1[i][-1]

    # display_hash(HashTable1)
    print(keyMapDict)
