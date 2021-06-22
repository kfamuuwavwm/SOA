import os
import sys
from ast import literal_eval

global extention_default

extention_default = {
	
	"html":"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nServer: nginx\r\n\r\n",

	"ico":"HTTP/1.1 200 OK\r\nContent-Type: image/x-icon; charset=utf-8\r\nServer: nginx\r\n\r\n",

	"css":"HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"scss":"HTTP/1.1 200 OK\r\nContent-Type: text/x-scss; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"woff":"HTTP/1.1 200 OK\r\nContent-Type: application/font-woff; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"woff2":"HTTP/1.1 200 OK\r\nContent-Type: application/font-woff2; charset=utf-8\r\nServer: nginx\r\n\r\n",

	"js":"HTTP/1.1 200 OK\r\nContent-Type: application/js; charset=utf-8\r\nServer: nginx\r\n\r\n",

	"jpeg":"HTTP/1.1 200 OK\r\nContent-Type: image/jpeg; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"jpg":"HTTP/1.1 200 OK\r\nContent-Type: image/jpeg; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"png":"HTTP/1.1 200 OK\r\nContent-Type: image/png; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"webp":"HTTP/1.1 200 OK\r\nContent-Type: image/webp; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"gif":"HTTP/1.1 200 OK\r\nContent-Type: image/gif; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"bmp":"HTTP/1.1 200 OK\r\nContent-Type: image/bmp; charset=utf-8\r\nServer: nginx\r\n\r\n",

	"doc":"HTTP/1.1 200 OK\r\nContent-Type: application/msword; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"xls":"HTTP/1.1 200 OK\r\nContent-Type: application/ms-excel; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"pdf":"HTTP/1.1 200 OK\r\nContent-Type: application/pdf; charset=utf-8\r\nServer: nginx\r\n\r\n",
	"txt":"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream; charset=utf-8\r\nServer: nginx\r\n\r\n",

	"exe":"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream; charset=utf-8\r\nServer: nginx\r\n\r\n",

	"mp3":"HTTP/1.1 200 OK\r\nContent-Type: audio/mpeg3; charset=utf-8\r\nServer: nginx\r\n\r\n",

	"zip":"HTTP/1.1 200 OK\r\nContent-Type: application/x-zip-compressed; charset=utf-8\r\nAccept-Ranges: bytes\r\nServer: nginx\r\n\r\n",
	"7z":"HTTP/1.1 200 OK\r\nContent-Type: application/x-7z-compressed; charset=utf-8\r\nAccept-Ranges: bytes\r\nServer: nginx\r\n\r\n"

}

extention_default_else = "HTTP/1.1 200 OK\r\nContent-Type: charset=utf-8\r\nServer: nginx\r\n\r\n"

def create_server():

	path_ascii_add = 0

	switch_db = {}
	ret_switch_code = ""

	pre_pwd = "../../front_end/"
	create_server_ret_data = ""
	create_server_ret_data_2 = ""
	path_filename2 = ""
	path_filename2_pwd = ""

	for ( path, dir, files ) in os.walk(pre_pwd):

		for filename in files:

			pre_path_filename = path + "/" + filename

			path_filename = pre_path_filename
			path_filename = path_filename.replace("../../front_end","").replace("//","/")
			
			path_filename2 = pre_path_filename
			path_filename2 = path_filename2.replace("//","/")

			pre_result_extention = path_filename.split(".")

			try:

				rsp_header = extention_default[path_filename.split(".")[-1]]

				if path_filename.split(".")[-1] in extention_default.keys():

					f = open(path_filename2,"r")
					file_read_ret = f.read()
					f.close()

					f = open(path_filename2,"w")
					f.write(rsp_header + file_read_ret)
					f.close()

			except:

				f = open(path_filename2,"r")
				file_read_ret = f.read()
				f.close()

				f = open(path_filename2,"w")
				f.write(extention_default_else + file_read_ret)
				f.close()

			for i in range( 0,len(path_filename.replace("index.html","")) ):

				path_ascii_add += int(ord(path_filename.replace("index.html","")[i]))		


			if path_filename == "/index.html":

				path_filename2_pwd = pre_pwd[:-1] + path_filename


			pre_create_server_ret_data = '               else if ( strcmp(strcut_arr[1], "'
			pre_create_server_ret_data += path_filename.replace("index.html","") + '") == 0 ){\n\n'
			pre_create_server_ret_data += '                  FILE * f = fopen("' + pre_pwd[:-1] + path_filename + '", "r");\n'
			pre_create_server_ret_data += '                  fseek(f, 0, SEEK_END);\n'
			pre_create_server_ret_data += '                  f_size = ftell(f);\n'
			pre_create_server_ret_data += '                  file_buffer = malloc(f_size);\n'
			pre_create_server_ret_data += '                  memset(file_buffer, 0, f_size);\n'
			pre_create_server_ret_data += '                  fseek(f, 0, SEEK_SET);\n'
			pre_create_server_ret_data += '                  fread(file_buffer, f_size, 1, f);\n'
			pre_create_server_ret_data += '                  fclose(f);\n'
			pre_create_server_ret_data += '                  write(cs, file_buffer, f_size);\n'
			pre_create_server_ret_data += '                  close(cs);\n'
			pre_create_server_ret_data += '                  free(file_buffer);\n'
			pre_create_server_ret_data += '               }\n'

			create_server_ret_data = pre_create_server_ret_data



			path_ascii_add = str(path_ascii_add)

			if path_ascii_add in switch_db.keys():

				pre_switch_db = switch_db[path_ascii_add]
				pre_switch_db.append(create_server_ret_data)

				switch_db[path_ascii_add] = pre_switch_db

			else:

				switch_db[path_ascii_add] = [ create_server_ret_data ]

			path_ascii_add = 0



	for path_ascii_add_2 in switch_db.keys():

		pre_create_server_ret_data_2 = "\n            case "
		pre_create_server_ret_data_2 += str(path_ascii_add_2) + ":\n"
		pre_create_server_ret_data_2 += '            {\n'

		for key_len in range(0,len(switch_db[path_ascii_add_2])):

			if key_len == 0 :

				pre_create_server_ret_data_2 += switch_db[path_ascii_add_2][key_len].replace("else if (","if (")


			else:

				pre_create_server_ret_data_2 += switch_db[path_ascii_add_2][key_len]
				     

		pre_create_server_ret_data_2 += "               else{\n"
		pre_create_server_ret_data_2 += '                  write( cs , error , sizeof(error) );\n'
		pre_create_server_ret_data_2 += '                  close(cs);\n'
		pre_create_server_ret_data_2 += "               }\n"
		pre_create_server_ret_data_2 += "               break;\n"
		pre_create_server_ret_data_2 += '            }\n'

		create_server_ret_data_2 += pre_create_server_ret_data_2


	# index.html
	pre_create_server_ret_data_3 = "\n            case "
	pre_create_server_ret_data_3 += "1066:\n"
	pre_create_server_ret_data_3 += '            {\n'
	pre_create_server_ret_data_3 += '               if ( strcmp(strcut_arr[1], "/index.html") == 0 ){\n\n'
	pre_create_server_ret_data_3 += '                  FILE * f = fopen("' + path_filename2_pwd + '", "r");\n'
	pre_create_server_ret_data_3 += '                  fseek(f, 0, SEEK_END);\n'
	pre_create_server_ret_data_3 += '                  f_size = ftell(f);\n'
	pre_create_server_ret_data_3 += '                  file_buffer = malloc(f_size);\n'
	pre_create_server_ret_data_3 += '                  memset(file_buffer, 0, f_size);\n'
	pre_create_server_ret_data_3 += '                  fseek(f, 0, SEEK_SET);\n'
	pre_create_server_ret_data_3 += '                  fread(file_buffer, f_size, 1, f);\n'
	pre_create_server_ret_data_3 += '                  fclose(f);\n'
	pre_create_server_ret_data_3 += '                  write(cs, file_buffer, f_size);\n'
	pre_create_server_ret_data_3 += '                  close(cs);\n'
	pre_create_server_ret_data_3 += '                  free(file_buffer);\n'
	pre_create_server_ret_data_3 += '               }\n'     
	pre_create_server_ret_data_3 += "               else{\n"
	pre_create_server_ret_data_3 += '                  write( cs , error , sizeof(error) );\n'
	pre_create_server_ret_data_3 += '                  close(cs);\n'
	pre_create_server_ret_data_3 += "               }\n"
	pre_create_server_ret_data_3 += "               break;\n"
	pre_create_server_ret_data_3 += '            }\n'

	create_server_ret_data_2 += pre_create_server_ret_data_3


	return create_server_ret_data_2


if __name__ == '__main__':

	bind_port = sys.argv[1]

	os.system("rm -rf ../../front_end")
	os.system("unzip ../../front_end.zip -d ../../front_end")

	f = open("./file/server_top.txt","r")
	server_top = f.read()
	f.close()

	f = open("./file/server_middle.txt","r")
	server_middle = f.read()
	f.close()

	f = open("./file/server_bottom.txt","r")
	server_bottom = f.read()
	f.close()
	
	data = server_top
	data += bind_port
	data += server_middle

	data += create_server()

	data += server_bottom
	
	f = open("run.c","w")
	f.write(data)
	f.close()

	os.system("./build > gcc.log 2>&1")