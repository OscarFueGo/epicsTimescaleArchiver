import epics
import time
import psycopg2
import datetime
import sys

# Replace with your actual database connection details
dbname = 'softioc'
user = 'software'
password = 'admin'
host = 'timescaledb'  # Or the IP address of your PostgreSQL server
port = '5432'  # Default PostgreSQL port



def writeTs(channel_name, freq):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cur = conn.cursor()
    channel = epics.PV(channel_name)
    try:
        while True:
            # Get the current value of the channel
            value = channel.get()
            print(value)
            now = datetime.datetime.now()
            insert_query = "INSERT INTO softioc (time, channel, value, status) VALUES (%s, %s, %s, %s);"
            data = (now,channel_name,value,"active")
            cur.execute(insert_query, data)
            conn.commit()
            time.sleep(freq)
            
    except KeyboardInterrupt:
        print("Interrupted by user, exiting...") 
        cur.close()
        conn.close()

if __name__ == "__main__":
    # Arguments start from sys.argv[1], as sys.argv[0] is the script name
    channelName = sys.argv[1]  # First argument
    channelFreq = sys.argv[2]  # Second argument
    print(f"Argument 1: {channelName}")
    print(f"Argument 2: {channelFreq}")
    writeTs(channelName, int(channelFreq))
