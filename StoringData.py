import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import mysql.connector
from mysql.connector import Error
import json

class StoringData(commands.Cog):
    def __init__(self, client):
        self.client = client
    testServerId=1223345494353248317
    
    @nextcord.slash_command(name="store_info",description="store some data",guild_ids=[testServerId])
    async def store_info(self,interaction:Interaction,message:str):
        #todos comandos en minusculas
        guild= interaction.guild.id
        try:
            connection=mysql.connector.connect(host='localhost',database='youtube_bot',user='root',password='root')
            cursor=connection.cursor()

            mySql_Create_Table_Query= """CREATE TABLE IF NOT EXISTS DB_{} (
                                    Id INT AUTO_INCREMENT PRIMARY KEY,
                                    User VARCHAR(250) NOT NULL,
                                    Message VARCHAR(5000) NOT NULL)""".format(guild)
            
            cursor.execute(mySql_Create_Table_Query)
            print("Guild ({}) TABLE CREATED CORRECTLY".format(guild))
        except mysql.connector.Error as error:
            print("Failed to create table: {}".format(error))
        finally:
            if 'connection' in locals() and connection.is_connected():
                table= "DB_"+str(guild)
                mySql_Insert_Row_Query="INSERT INTO "+table+" (User,Message) VALUES (%s,%s)"
                mySql_Insert_Row_values=(str(interaction.user),message)
                cursor.execute(mySql_Insert_Row_Query,mySql_Insert_Row_values)
                connection.commit()
                await interaction.response.send_message("I have stored your message for you")
                cursor.close()
                connection.close()
                print("MySQL connection has been closed")
    @nextcord.slash_command(name="retrive_info",description="retrive some data",guild_ids=[testServerId])
    async def retrive_info(self,interaction:Interaction):
        guild=interaction.guild.id
        table= "DB_"+str(guild)
        try:
            connection=mysql.connector.connect(host='localhost',database='youtube_bot',user='root',password='root')
            cursor=connection.cursor()
            sql_select_query = "SELECT * FROM " + table + " WHERE user LIKE '%" + str(interaction.user) + "%'"

            cursor.execute(sql_select_query)
            record = cursor.fetchall()
            Received_Data= []
            for row in record:
                Received_Data.append({"Id":str(row[0]),"Message":str(row[2])})
            await interaction.response.send_message("All stored data:\n \n"+json.dumps(Received_Data,indent=1))
        except mysql.connector.Error as error:
            print("failed to get record from mysql table:{}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("mysql conection is closed")


def setup(client):
    client.add_cog(StoringData(client))
