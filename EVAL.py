import prompt


class Input:

	def __init__(self):
		self.types = {1: "IPv4", 2: "IPv6"}
		self.type = None

		choosentype = self.gettype()

		if choosentype == 1:
			self.ipv4_eval()
		elif choosentype == 2:
			self.ipv6_eval()
		else:
			exit('Test')

	def gettype(self):

		def icon():
			print(
					"                                        `.-:/+ooooooo++/:-.                                               ")
			print(
					"                                  -/oydNMMMMMMMMMMMMMMMMMMMMmdyo:.                                        ")
			print(
					"                             ./sdNMMMMNmdhyso++//////++osyhdmNMMMMNho:`                                   ")
			print(
					"                          :smMMMMmhyo:-.`.` ./:/. o-  -` ..`..:+shmMMMNdo-                                ")
			print(
					"                       :yNMMMmho:.`-:. hs: :N`    M:  s.`N/ss ./``.:oymMMMmo-                             ")
			print(
					"                    .omMMMms/.`   :h-- om:-/M.   `M:  h omys- ds :so:../sdMMMd+`                          ")
			print(
					"                  -yNMMNy/.`:.     /osm`No/.-+::-`-+:/. y:od om  :N-.`s-`./ymMMNo`                        ")
			print(
					"                .yMMMmo-`   /m:     /:/`.-/+osyyyyyyyyso+/-../. :N-  `M::/ `-odMMNs`                      ")
			print(
					"              `sMMMmo.` /ds:`.mo/-`.:oyhmmmmmmmmmmmmmmmmmmmmhyo:..  `yh:     `.+dMMN+                     ")
			print(
					"             :mMMNo-`-`  y+syy.:-+ydmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy+--/       -/`-omMMd.                   ")
			print(
					"            sMMMh:`  `/+..s  .+ymmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmh+.  //s+mo  `:yMMN+                  ")
			print(
					"          `dMMNo- :hyyyyd+..odmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddhhdmmmmmds-  `Ns .-- .+NMMs                 ")
			print(
					"         .mMMm/. ..-++`  .odmmmmdhhhhhdmmmmd+//:-.-ymmmmmdyssssssshmmmmmdo..o.dh+/+:`/mMMh`               ")
			print(
					"        .mMMm:`:++sdy`:`/hmmmmdyssssssssdmmdhs+:.  .mmmmmhsssssssyyymmmmmmd/`:o    +``:dMMh               ")
			print(
					"       `dMMm:` d`   y-.ommmmmhyyyhhhhysydmmmmmo    -dmmmmdhsyhmhhdyyymmmmmmms.:od/ .//`:mMMs              ")
			print(
					"       yMMN/.  /dyo+/.ymmmmmdsshyyhhhyshmmmmmh`` ` .smmmmmyyydhhyyhsyhmmmmmmmy- /yhd/+/`/NMM/             ")
			print(
					"      :MMMo- ohy+:. .ymmmmmmhyyhyyhyhyshmmmmm/..-`-`+mmmdyssddyhdhydssdmmmmmmmy--s .. ...+MMN`            ")
			print(
					"      dMMd: +` `:++.smmmmmmmyydyhhyyddssssoo+--:--:-:ooo+shyddyyydddddhmmmmmmmms.`///hN- :hMMs            ")
			print(
					"     :MMM+.`dyys+: /mmmmmmmdhhdddhhhsddys+:::::::::::::::ydmyydhydydshymmmmmmmmm+`  sd`  ./MMN`           ")
			print(
					"     yMMm: ..  `--.ymmmmmmmhyshyhmyyyhydd++/:o-+/-o:/+-+:yhydyydddsdshymmmmmmmmmh- hd///- :dMM/           ")
			print(
					"     NMMy- `-/oyh :mmmmmmmmhhsdsyhhmhydyy/s/-h oo`h-/s y:yhdhdhmsmsdsyhdmmmmmmmmm/ `ohhy/ -sMMy           ")
			print(
					"    `MMMo. ohyy. `ommmmmmmmyhsdshysdhmhhhss/-h oo`h-/s yohmdhmsmsdsdsshdmmmmmmmmmo`s-   :/.+MMm           ")
			print(
					"    -MMM+.   `:/:`smmmmmmmmyhsdshsshyhsdddd/-h oo`h-/s yyddhsmsmsdydyshdmmmmmmmmms.:.   --./MMN           ")
			print(
					"    -MMM+.`///yd/`smmmmmmmmsdydsdsyhyhsdhhho:h oo`h-/s-hydydsdyhyhhymyhhmmmmmmmmms.`` ./s:./MMN           ")
			print(
					"    `MMMo.  -dy. `ommmmmmmmyhmysdsyhhyyddhhyhy oo`h-/hhhhmmmsydydymshhyymmmmmmmmmo`:syhs. .+MMm           ")
			print(
					"     NMMy- smo/// /mmmmmmmmyhdshhshydyymmmyyhyo++.y:yyyyhmmmdsmsdsymhshsdmmmmmmmm/     `/`-sMMy           ")
			print(
					"     :MMM/.    `  `+mmmmmmmmdyhdshdsmymmmhyyyh+..`..+hhsydmmmmydsdhdhyymmmmmmmmm+` -`/   ./MMN`           ")
			print(
					"      dMMh:  .:o:. .smmmmmmmdhhhyNyyddmmmhhyys:`````:shyshmmmmmydymyydmmmmmmmmmy.  :o+-` -yMMs            ")
			print(
					"      :MMM+.  -::`  -hmmmmmmmmhydhsmhmmmmsshyh-`````.ysyssdmmmmmmhhdyymmmmmmmmh-     -  .+MMN`            ")
			print(
					"       yMMm:`        -hmmmmmmmydyyhdmmmmhyhyss.`` ```ssysshmmmmmdshsdshmmmmmmh:        `:mMM/             ")
			print(
					"      `dMMd:`     `  -ymmmmmmhhsshhhhyoo+++so:..`...++/++/+hy+y/ydmms+hmmmmy-  :++/- `:hMMs               ")
			print(
					"        .mMMh:`  /s+`  `+dmmmd+++/////+/++o:::/::::://:/++++++//+dmmmdhodmdo. `- :o.``:hMMh               ")
			print(
					"          `dMMm/. `-:os ` `:ymmo//yo/+hmmmmmmmmmmmmmmmmmmmmmmmmmmdsooymy:`  .sos+:`./mMMs                 ")
			print(
					"            sMMNs-`  ss:++` `-ohmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmds-`  +oh./o `-sNMN+                  ")
			print(
					"             :mMMd+. .-y/`y+.  `:shmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmhs:`   o/:+do/ ./dMMd.                   ")
			print(
					"              `sNMMh/.  .y-.h/--  `-+shdmmmmmmmmmmmmmmmmmmmmdhs+-`  ` `d/ss:` ./hMMN+                     ")
			print(
					"                .yMMMh/.` .h--y/-o    `.-/+syyhhhddhhhyys+/-.`   .- osoo+/``./hNMNs`                      ")
			print(
					"                  -yNMMdo-. `/+-so -s:.:-`    ````````      .:.  :yy//`. `-odMMNo`                        ")
			print(
					"                    .omMMNho-.``  `.y/ d-`-h .o/-/----  s-:y/d:` .: .`.-ohNMMd+`                          ")
			print(
					"                     :yNMMNds/-.`.- -o /:h: d.:h-:so `m- s::-  `../sdNMMmo-                               ")
			print(
					"                        :smMMMNdyo:-.``  .. / .+-.-/   --``..:oydNMMNdo-                                  ")
			print(
					"                           `/sdNMMMNmhyso+/::------::/+osyhmNMMMNho:`                                     ")
			print(
					"                                  -/oydNMMMMMMMMMMMMMMMMMMMMmdyo:.                                        ")
			print(
					"                                       `.-:/++osssso++/:-.                                                ")
			print(
					"                                                                                                          ")
			icon()

		entryNotChoosen = True

		print('\t \n Which header do you like to insert? \n')
		print('1: IPv4 \n')
		print('2: IPv6 \n')

		while entryNotChoosen:
			type = prompt.integer('Header Version Type: ')

			if type in self.types:
				self.type = type

				entryNotChoosen = False

		return self.type

	def ipv4_eval(self):
		print("\n Selected IP Version 4 (Please hit enter)")
		self.gettype = prompt.integer("\n IP Version: ...")  # ip version 4bit
		ihl = prompt.integer("\n Internet Header Lenght ")  # header lenght 4bit
		tos = prompt.integer("\n Type-of-Service ")  # type of service 8bit
		total_len = prompt.integer("\n Total Length ")  # max. lenght 16bit
		identifiction = prompt.integer("\n Identifiction ")  # number of packet 16bit
		flags = prompt.integer("\n Flag ")  # 3bit
		frags = prompt.integer("\n Fragment-Offset ")  # regarding to mf flag 14bit
		ttl = prompt.integer("\n Time-to-Live ")  # 8bit time to live
		protocol = prompt.integer("\n Protocol")  # 8bit protocol type
		checksum = prompt.integer(" \n Header Checksum ")  # 16bit header verfification
		sourceip = prompt.regex("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", prompt='Source Address: ')
		destip = prompt.regex("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", prompt='Destination Address: ')
		opt_pad = prompt.integer("\n Options ")

		return{
				"IP Version": self.gettype(),
				"Internet Header Lenght": ihl,
				"Type-of-Service": tos,
				"Total Length": total_len,
				"Identifiction": identifiction,
				"Flags": flags,
				"Fragment-Offset": frags,
				"Time-to-Live": ttl,
				"Protocol": protocol,
				"Header Checksum": checksum,
				"Source Address": sourceip,
				"Destination Address": destip,
				"Options": opt_pad
			}

	def ipv6_eval(self):
			print("\n Selected IP Version 6 (Please hit enter)")
			self.gettype = prompt.integer("\n IP Version 6 ")  # ip version 4bit
			traffic_class = prompt.integer("\n Traffic Class ")  # quality of service 8bit
			flow_label = prompt.integer("\n Flow Label ")  # flow label 20bit
			payload_len = prompt.integer("\n Payload Lenght ")  # Data Legnth in Packet 16bit
			next_header = prompt.integer("\n Next Header ")  # identificates next header 8bit
			hop_limit = prompt.integer("\n Hop Limit ")  # max. amount of hops 8bit
			src_address = prompt.regex("^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", prompt="\n Source Address ")  # 128bit
			dest_address = prompt.regex("^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", prompt="\n Destination Address ")  # 128bit
			ext_header = prompt.integer("\n Header Extension ")

			return {
				"IP Version": self.gettype(),
				"Traffic Class": traffic_class,
				"Flow Label": flow_label,
				"Payload Lenght": payload_len,
				"Next Header": next_header,
				"Hop Limit": hop_limit,
				"Source Address": src_address,
				"Destination Address": dest_address,
				"Header Extension": ext_header
			}