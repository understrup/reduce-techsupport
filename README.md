The output from the command 'show tech-support' consist of 400-450 show like the exsamples below:

	`show switchname`
	`show system uptime`
	`show interface mgmt0`
	`show system resources`
	`show version `

resulting in a file with 520.000 to 600.000 lines depending on the platform.

"reduce-techsupport.py" can reduce number of lines by applying filters to the output.

 Filter = "system uptime;show version" will give output:
 
 `show switchname` 
 
 `show system uptime`
	System start time:          Sun Apr  3 13:50:24 2016
	System uptime:              536 days, 17 hours, 47 minutes, 50 seconds
	Kernel uptime:              536 days, 18 hours, 13 minutes, 2 seconds
	Active supervisor uptime:   536 days, 17 hours, 47 minutes, 50 seconds
	
 `show interface mgmt0`
 
 `show system resources`
 
 `show version `

    Cisco Nexus Operating System (NX-OS) Software
    TAC support: http://www.cisco.com/tac
    Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
    Copyright (c) 2002-2015, Cisco Systems, Inc. All rights reserved.
    The copyrights to certain works contained herein are owned by
    other third parties and are used and distributed under license.
    Some parts of this software are covered under the GNU Public
    License. A copy of the license is available at
    http://www.gnu.org/licenses/gpl.html.
    
    Software
      BIOS:      version 3.6.0
      loader:    version N/A
      kickstart: version 6.0(2)N2(7)
      system:    version 6.0(2)N2(7)
      Power Sequencer Firmware: 
                 Module 1: version v5.0
                 Module 2: version v1.0
                 Module 3: version v1.0
                 Module 4: version v1.0
      Microcontroller Firmware:        version v1.0.0.2
      SFP uC:    Module 1: v1.0.0.0
      QSFP uC:   Module not detected
      BIOS compile time:       05/09/2012
      kickstart image file is: bootflash:///n5000-uk9-kickstart.6.0.2.N2.7.bin
      kickstart compile time:  4/28/2015 5:00:00 [04/28/2015 15:37:44]
      system image file is:    bootflash:///n5000-uk9.6.0.2.N2.7.bin
      system compile time:     4/28/2015 5:00:00 [04/28/2015 17:53:45]
    
    
    Hardware
      cisco Nexus 5596 Chassis ("O2 48X10GE/Modular Supervisor")
      Intel(R) Xeon(R) CPU         with 8253868 kB of memory.
      Processor Board ID FOC172447T4
    
      Device name: dc1-srvacc-01
      bootflash:    2007040 kB
    
    Kernel uptime is 536 day(s), 18 hour(s), 13 minute(s), 4 second(s)
    
    Last reset at 907924 usecs after  Sun Apr  3 13:46:00 2016
    
      Reason: Disruptive upgrade
      System version: 6.0(2)N2(1)
      Service: 
    
    plugin
      Core Plugin, Ethernet Plugin
    `dir bootflash:`
              0    Jan 01 07:19:46 2009  20090101_061946_poap_4755_init.log
              0    Jan 01 07:38:51 2009  20090101_063851_poap_4680_init.log
              0    Feb 21 12:51:31 2009  20090221_115131_poap_4694_init.log
        4515014    Jan 27 12:55:12 2014  TAC-PAC_dc1-srvacc-01.txt
            248    Feb 22 09:56:51 2009  convert_pfm1.log
          10240    Dec 09 12:00:51 2013  dc1-srvacc-01-license.tar
            342    Feb 22 09:56:51 2009  fcoe_mgr_cnv.log
           1123    Feb 22 09:55:48 2009  fwm_pre_issu_dump.txt
            267    Jan 01 07:22:23 2009  license_FOX1725GKF4_5_1.lic
           4096    Apr 03 13:47:44 2016  lost+found/
       34672128    Jul 08 08:13:20 2013  n5000-uk9-kickstart.6.0.2.N1.2.bin
       35589120    Feb 22 09:49:55 2009  n5000-uk9-kickstart.6.0.2.N2.1.bin
       35515392    Mar 18 12:02:02 2016  n5000-uk9-kickstart.6.0.2.N2.7.bin
       34799104    Sep 17 15:23:16 2017  n5000-uk9-kickstart.7.1.4.N1.1.bin
      238082390    Jul 08 08:15:03 2013  n5000-uk9.6.0.2.N1.2.bin
      244168123    Feb 22 09:51:10 2009  n5000-uk9.6.0.2.N2.1.bin
      229979876    Mar 18 11:37:33 2016  n5000-uk9.6.0.2.N2.7.bin
      327996211    Sep 17 15:22:22 2017  n5000-uk9.7.1.4.N1.1.bin
       11012259    Jan 27 13:22:37 2014  show-tech-fa-is_dc1-srvacc-01.txt
       12545701    Jan 27 13:39:13 2014  show-tech-fa-sw_dc1-srvacc-01.txt
       11794224    Jan 27 13:36:23 2014  show-tech-fa-to_dc1-srvacc-01.txt
        3403730    Jan 27 13:45:41 2014  show-tech-fwm_dc1-srvacc-01.txt
           4542    Feb 22 09:55:48 2009  stp.log.1
           4096    Jan 01 07:18:21 2009  vdc_2/
           4096    Jan 01 07:18:22 2009  vdc_3/
           4096    Jan 01 07:18:22 2009  vdc_4/
            641    Feb 22 09:56:51 2009  vfc_cnv.log
           4096    Jan 01 07:18:22 2009  virt_strg_pool_bf/
    
    Usage for bootflash://sup-local
     1342889984 bytes used
      308015104 bytes free
     1650905088 bytes total
