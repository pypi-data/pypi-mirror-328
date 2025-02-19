"""Initialize a timetracker project"""

__copyright__ = 'Copyright (C) 2025-present, DV Klopfenstein, PhD. All rights reserved.'
__author__ = "DV Klopfenstein, PhD"

from sys import exit as sys_exit
from os.path import exists
#from os.path import abspath
#from os.path import relpath
from os.path import dirname
from logging import debug

##from timeit import default_timer
##$from datetime import timedelta
from datetime import datetime
from timetracker.msgs import str_started
#from timetracker.msgs import str_notrkrepo
from timetracker.msgs import str_init
from timetracker.utils import yellow
from timetracker.cfg.cfg_local  import CfgProj


def cli_run_start(fnamecfg, args):
    """Initialize timetracking on a project"""
    run_start(
        fnamecfg,
        args.name,
        #args.project,
        #args['csvdir'],
        args.force,
        args.quiet)

def run_start(fnamecfg, name=None, force=False, quiet=False):
    """Initialize timetracking on a project"""
    debug(yellow('START: RUNNING COMMAND START'))
    now = datetime.now()
    if not exists(fnamecfg):
        print(str_init(dirname(fnamecfg)))
        sys_exit(0)
    cfgproj = CfgProj(fnamecfg)
    start_obj = cfgproj.get_starttime_obj(name)
    fin_start = start_obj.filename
    # Is this project tracked?
    ###if not exists(cfgproj_fname):
    ###    print(str_notrkrepo(dirname(dirname(cfgproj_fname))))
    ###    sys_exit(0)
    # Print elapsed time, if timer was started
    start_obj.prt_elapsed()
    # Set/reset starting time, if applicable
    if not exists(fin_start) or force:
        #cfgproj.mk_workdir()
        #cfgproj.update_localini(project, csvdir)
        #cfgproj.wr_cfg()
        #cfg_global = CfgGlobal()
        #chgd = cfg_global.add_proj(cfgproj.project, cfgproj.get_filename_cfgproj())
        #if chgd:
        #    cfg_global.wr_cfg()
        with open(fin_start, 'w', encoding='utf8') as prt:
            prt.write(f'{now}')
            if not quiet:
                print(f'Timetracker {"started" if not force else "reset to"} '
                      f'{now.strftime("%a %I:%M %p")}: {now} '
                      f"for project '{cfgproj.project}'")
            debug(f'  WROTE: {fin_start}')
    # Informational message
    elif not force:
        print(str_started())
    return fin_start


    #dirtrk = kws['trksubdir']
    #if not exists(dirtrk):
    #    makedirs(dirtrk, exist_ok=True)
    #    absdir = abspath(dirtrk)
    #    print(f'Initialized timetracker trksubdir: {absdir}')
    #    fout_cfg = join(absdir, 'config')
    #    with open(fout_cfg, 'w', encoding='utf8') as ostrm:
    #        print('', file=ostrm)
    #        print(f'  WROTE: {relpath(fout_cfg)}')


#class CmdStart:
#    """Initialize a timetracker project"""
#    # pylint: disable=too-few-public-methods
#
#    def __init__(self, cfgfile):
#        self.cfgfile = cfgfile


# Copyright (C) 2025-present, DV Klopfenstein, PhD. All rights reserved.
