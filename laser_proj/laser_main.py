import sqlite3
import os.path 
import time
import json
import http
from lib.lib_log import log_info
def dum_print(*args, **kwargs):
    pass

laser_table = {
    "operator_table":       {"id":" integer",  "operator_name" :" varchar(128)", },
    "custom_table":         {"id": " integer",    "custom_name":" varchar(128)", },
    "print_type_table":     {"id":" integer", "type_name":" varchar(128)", },
    "print_record_table":   {"id":" integer", "custom_id":" integer",
                            "type_id":" integer", "operator_id":" integer",
                            "print_time_s":" integer", "print_info":" TEXT"},  
}


class laser_main():
    def __init__(self, parent=None):
        self.orig_data              = None;
        self.debug                  = True;
        self.root_path              = os.path.split(os.path.realpath(__file__))[0];
        self.config_path            = self.root_path+"\\config.cfg" 
        self.to_laser_file          = self.root_path+"\\tttttt.txt" 
        print(self.root_path)       
        self.config_data            = {};

        print(self.config_path)
        if False == os.path.exists(self.config_path):
            print("+++")
            config = open(self.config_path, 'w')
            config.close();

        self.init_config();
        self.save_config();
        self.init_ds();
        log_info.output("laser_main_init")
            
    def init_config(self):
        self.config_data["user_file_path"]      = self.root_path; #输出的位置
        self.config_data["user_excel_file"]     = None; #"sl_null";      #上次的文件地址 
        self.config_data["user_select_index"]   = None# "sl_null";      #上次的index
        self.config_data["user_operator_name"]  = None#"sl_null";      #商城的操作员名字
        self.config_data["user_custom_name"]    = None#"sl_null";      #商城的操作员名字
        self.config_data["user_begin_index"]    = None#sl_null";      #上次的起始index
        self.config_data["user_end_index"]      = None#"sl_null";      #上次的结束index

        config_hdl = open(self.config_path);
        config_txt = config_hdl.read();
        config_hdl.close()
        try:
            json_dic1 = json.loads(config_txt)
        except:
            print("文件异常");
            json_dic1 = None;

        if json_dic1 is not None:
            for key in json_dic1:  
                #if json_dic1[key] is not None:
                self.config_data[key] = json_dic1[key] 

    def save_config(self):
        config_txt = json.dumps(self.config_data)
        #print(config_txt);
        config_hdl = open(self.config_path, 'w')
        config_hdl.write(config_txt);
        config_hdl.close();

    def set_config(self, config_name, config_value):
        self.config_data[config_name] = config_value;
        self.save_config();

    def get_config(self, config_name):
        if config_name in self.config_data.keys():
            return self.config_data[config_name]
        else:
            print(config_name + " is not in keys")
            return None
#--------------------------------------------------------------------------------------------
    def init_ds(self):
        self.ds_conn = sqlite3.connect("laser.db");
        self.cu = self.ds_conn.cursor() 
        #CommandText = "SELECT COUNT(*) FROM sqlite_master where type='table' and name='operator_table'";
        for key_table in laser_table: 
            try:
                command_check_table_str = "select count(*)  from sqlite_master where type='table' and name = '"+ key_table +"' " 
                self.cu.execute(command_check_table_str);
                find_result = str(self.cu.fetchone())
                print(type(find_result));
                print(find_result);
                find_result = tuple(eval(find_result));
                if 0 == find_result[0]:
                    print("create table")
                    command_create_table_str = "create table  "+ key_table + " (id integer primary key autoincrement)"
                    # try: 
                    self.cu.execute(command_create_table_str);
                    self.ds_conn.commit()
                    print("success")               
                    # except:  
                    #     print ("Create table failed: " + key_table);
                    #     return False 
            except:
                print ("check table failed: " + key_table);
                return False             

            for key_col in laser_table[key_table]:
                try:      
                    command_check_col_str = "select * from sqlite_master where name='"
                    command_check_col_str = command_check_col_str + key_table + "' and sql like " 
                    command_check_col_str = command_check_col_str +"'%" + key_col  + "%'";  

                    self.cu.execute(command_check_col_str);
                    tmp_col_info = self.cu.fetchone()
                    if tmp_col_info is None: 
                        #print(tmp_col_info);
                        #ALTER TABLE 表名 ADD COLUMN 列名 数据类型 
                        # command_add_col_str = "alter table '"+ key_table +"' add column '" + key_col +"' "
                        # command_add_col_str = command_add_col_str + laser_table[key_table][key_col]
                        command_add_col_str = "alter table "+ key_table +" add column " + key_col +" "
                        command_add_col_str = command_add_col_str + laser_table[key_table][key_col]
                        #print(command_add_col_str)
                        # try:
                        self.cu.execute(command_add_col_str);
                        self.ds_conn.commit()
                        print("success add col:"+key_col) 
                        # except:
                        #     print ("add col failed: " + key_col);
                        #     return False 
                    else:
                        #print(tmp_col_info);
                        pass
                except:
                    print ("Create col failed_2" + key);
                    return False

    def insert_operator(self, operator_name):
        try:
            command = "select id from operator_table where operator_name = '" + operator_name +"'"
            self.cu.execute(command)
            is_find = self.cu.fetchone();
            if is_find is None :
                command = "insert into operator_table (operator_name) values ('" + operator_name + "')" 
                self.cu.execute(command)
                self.ds_conn.commit()
                return self.insert_operator(operator_name);
            else:
                print(str(is_find[0]))
                return int(is_find[0]);
        except:
            print("insert failed " + operator_name)
            return False
    
    def get_operator_name(self, id):
        try:
            command = "select operator_name from operator_table where id = " + str(id)
            self.cu.execute(command)
            is_find = self.cu.fetchone();
            if is_find is not None :
               return is_find[0]
            else:
                return "None"
        except:
            print("get_operator failed " + str(id))
            return False

    def get_all_operator_name(self):
        try:
            command = "select operator_name from operator_table"
            self.cu.execute(command)
            is_find = self.cu.fetchall();
            #print(is_find)
            if is_find is not None :
                return_find = [];
                for i in range(len(is_find)):
                    return_find.append(is_find[i][0])      
                return return_find
            else:
                return "None"
        except:
            print("get_all_operator_name failed")
            return False

    def get_part_operator_name(self, part_name):
        try:
            command = "select operator_name from operator_table where operator_name  like "  + "'%" + part_name + "%'"
            self.cu.execute(command)
            is_find = self.cu.fetchall();
            #print(is_find)
            if is_find is not None :
                return_find = [];
                for i in range(len(is_find)):
                    return_find.append(is_find[i][0])      
                return return_find
            else:
                return "None"
        except:
            print("get_all_operator_name failed")
            return False


    def insert_custom(self, custom_name):
        try:
            command = "select id from custom_table where custom_name = '" + custom_name +"'"
            self.cu.execute(command)
            is_find = self.cu.fetchone();
            if is_find is None :
                command = "insert into custom_table (custom_name) values ('" + custom_name + "')" 
                self.cu.execute(command)
                self.ds_conn.commit()
                return self.insert_custom(custom_name);
            else:
                print(str(is_find[0]))
                return int(is_find[0]);
        except:
            print("insert failed " + custom_name)
            return False

    def get_custom_name(self, id):
        try:
            command = "select custom_name from custom_table where id = " + str(id)
            self.cu.execute(command)
            is_find = self.cu.fetchone();
            if is_find is not None :
               return is_find[0]
            else:
                return "None"
        except:
            print("get_custom failed " + str(id))
            return False

    def get_all_custom_name(self):
        try:
            command = "select custom_name from custom_table "
            self.cu.execute(command)
            is_find = self.cu.fetchall();
            if is_find is not None :
                return_find = [];
                for i in range(len(is_find)):
                    return_find.append(is_find[i][0])      
                return return_find
            else:
                return "None"
        except:
            print("get_all_custom_name afaied " )
            return False

    def get_part_custom_name(self, part_name):
        try:
            command = "select custom_name from custom_table where custom_name like "  + "'%" + part_name + "%'"
            self.cu.execute(command)
            is_find = self.cu.fetchall();
            if is_find is not None :
                return_find = [];
                for i in range(len(is_find)):
                    return_find.append(is_find[i][0])      
                return return_find
            else:
                return "None"
        except:
            print("get_all_custom_name afaied " )
            return False




    def insert_print_type(self,type_name):
        try:
            command = "select id, type_name from print_type_table where type_name = '" + type_name +"'"
            self.cu.execute(command)
            is_find = self.cu.fetchone();
            if is_find is None :
                command = "insert into print_type_table (type_name) values ('" + type_name + "')" 
                self.cu.execute(command)
                self.ds_conn.commit()
                return self.insert_print_type(type_name);
            else:
                print(type(is_find))
                print(is_find)
                print(str(is_find[0]))
                return int(is_find[0]);
               
        except:
            print("insert failed " + type_name)
            return False

    def get_type_name(self, id):
        try:
            command = "select type_name from print_type_table where id = " + str(id)
            self.cu.execute(command)
            is_find = self.cu.fetchone();
            if is_find is not None :
               return is_find[0]
            else:
                return "None"
        except:
            print("get_print_type failed " + str(id))
            return False
    
    def get_all_type_name(self):
        try:
            command = "select type_name from print_type_table where id"
            self.cu.execute(command)
            is_find = self.cu.fetchall();
            if is_find is not None :
                return_find = [];
                for i in range(len(is_find)):
                    return_find.append(is_find[i][0])      
                return return_find
            else:
                return "None"
        except:
            print("get_print_type failed " + str(id))
            return False
    

    def insert_print_info(self,operator_id, type_id, custom_id, print_info ):
        now_time= int( time.time() );
        try:
            command = "insert into print_record_table (operator_id, custom_id, type_id, print_time_s, print_info ) values (" 
            command = command + str(operator_id) + ", " +str(custom_id) + ", " +str(type_id) + ", " + str(now_time) + ", "
            command = command + "'" + print_info + "')"
            self.cu.execute(command)
            self.ds_conn.commit()
            return True;
        except:
            print("insert failed " + print_info)
            return False

    def check_print_info(self, print_info):
        try:
            command = "select * from print_record_table where print_info = '"+print_info+"'"; 
            self.cu.execute(command);
            is_find = self.cu.fetchone();
            if is_find is None :
                return False;
            else:
                return True;
        except:
            print("check_print_info failed " + print_info)
            return False

    def get_print_info(self, para = ""):
        return_list = [];
        try:
            command = "select * from print_record_table" + para
            print("------: " + command);
            self.cu.execute(command);
            id = 0
            custom_name = ""
            type_name = ""
            operator_name = ""
            print_time = ""
            print_info = ""

            is_find = self.cu.fetchall();
            if is_find is None :
                return False;
            else:
                for i in range(len(is_find)):
                    id = is_find[i][0];
                    custom_name = self.get_custom_name(is_find[i][1])
                    type_name   = self.get_type_name(is_find[i][2])
                    operator_name = self.get_operator_name(is_find[i][3])
                    print_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(is_find[i][4]))
                    #print_time =time.ctime(is_find[i][4])
                    print_info = is_find[i][5]
                    tmp_tuple = (id, custom_name, operator_name, type_name, print_time, print_info)
                    return_list.append(tmp_tuple);
            return return_list;          
        except:
            print("get_print_info failed " + print_info)
            return False

    def del_all_print_info(self, para = ""):      
        try:
            command = "delete from print_record_table" 
            print("------: " + command);
            self.cu.execute(command);
            self.ds_conn.commit()
            return True      
        except:
            print("del_all_print_info failed ")
            return False


    #######################################################################################
    # def start_print(self, print_list):
    #     for print_item in print_list:  
    #         print(print_item);
    #         self.insert_print_info()

    def test_ds(self):
        self.insert_operator("huang")
        self.insert_operator("yin")
        self.insert_operator("ke")

        self.insert_custom("huang")
        self.insert_custom("yin")
        self.insert_custom("ke")

        self.insert_print_type("huang")
        self.insert_print_type("yin")
        self.insert_print_type("ke")

        self.insert_print_info(1, 2, 3,"huangxxxxxx")
        time.sleep(1)
        self.insert_print_info(11, 22, 3,"huangxxxxxx22")
        time.sleep(1)
        self.insert_print_info(12, 22, 23,"huangxxxxxx33333")


    
    def test_config(self,cfg_name, cfg_value):
        self.set_config(cfg_name, cfg_value);
        print(self.get_config(cfg_name));
        print(self.get_config("sdsdsd"))
        print(str(self.get_config("user_begin_index")) + "111111" )

    def test_all(self):
        test_config()

        
def test_laser_main():
    laser_main_x = laser_main();
    laser_main_x.test_config("huiii", "121212")
    laser_main_x.test_config("hutttii", 121212);

    laser_main_x.init_ds();