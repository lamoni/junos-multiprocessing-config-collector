# Author: Lamoni Finlayson
# Date: April 9th, 2019
# Purpose:
#   Boiler-plate code for multiprocessor command execution (in this instance, used for config collection)

from jnpr.junos.device import Device
import multiprocessing as mp
from multiprocessing import Pool

(username, password) = open('./credentials.txt').read().splitlines()


def retrieve_config(hostname):
    print "Starting: " + hostname

    session = Device(host=hostname, user=username, passwd=password)
    session.open()

    with open('./configs/%s' % hostname, 'w') as fp:
        fp.write(session.cli('show configuration | display set').strip())
        print "Finished: " + hostname


def retrieve_all_configs(hosts):
    pool = Pool(processes=mp.cpu_count())
    pool.map(retrieve_config, hosts)


retrieve_all_configs(open('./targets.txt').read().splitlines())
