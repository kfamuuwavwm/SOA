<br>

<p align="center">
    <img src="https://github.com/ENNP/soa/blob/main/readme/1.PNG" width="400">    
</p>

<br>

# SOA
**Automatically convert to a secure web server with html, css, js, img, etc.**

- SOA is simple to use.
- SOA servers are developed in the C language, they are fast to process.
- SOA provides a secure web server that can operate without a web firewall.

<br>

## To Use

- #### 1. front_end.zip
  - html, css, js, img ...   ->   front_end   ->   front_end.zip
  - Any folder structure is possible , SOA will scan everything.

    ![](https://github.com/ENNP/soa/blob/main/readme/2.PNG)

<br>

- #### 2. Run & Stop ( Required python 2.7 )
<p align="center">    
    <img src="https://github.com/ENNP/soa/blob/main/readme//how_to_soa.gif" width="770" >
</p>

<br>

## Security & optimization
- #### 1. switch ( ascii )
  - Check ascii code
    - Enhanced security by converting incoming input values to ascii code

      ![](https://github.com/ENNP/soa/blob/main/readme/3.PNG)

<br>

- #### 2. Attach HTTP Header Dictionary to File
  - TCP/IP & HTTP Comprehension Required 
    - Pre-attach HTTP headers and files
    - SOA does not put HTTP headers every time, but puts them in advance.

      ![](https://github.com/ENNP/soa/blob/main/readme/4.PNG)
      
      ![](https://github.com/ENNP/soa/blob/main/readme/5.PNG)
      
<br>

- #### 3. Secure "tcp no data connection vulnerability"
  <pre><code>
  // https://github.com/ENNP/SOA/blob/main/soa_file/run/start.c
  while(1){

		system("pkill -9 run");
		system("./run &");
		sleep(10);

  } 
  </code></pre>
  
<br>

## Thanks
- #### Sample Web Server ( front_end.zip )
  - Read Only by HTML5 UP
  - [html5up.net](https://html5up.net) | @ajlkn
  - Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)

<br>

## License
- #### [MIT License](https://github.com/ENNP/soa/blob/main/LICENSE)
