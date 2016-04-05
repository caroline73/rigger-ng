#coding=utf8
import  logging
import  utls.tpl ,interface ,base.tc_tools
# import  impl.rg_args
import  impl.rg_run 
import  impl.rg_utls
import  time 

_logger = logging.getLogger()

class crontab_tc(base.tc_tools.rigger_tc):
    def setUp(self):
        self.conf = utls.rg_var.value_of("${PRJ_ROOT}/src/extends/res/centos/tc/other_res.yaml")

    def test_shell(self) :
        # mock = base.tc_tools.res_mock()
        # with   mock :
        impl.rg_run.run_cmd("conf,start -s crontab -e dev,base",self.conf)
        impl.rg_run.run_cmd("conf,stop  -s crontab -e dev,base",self.conf)

    def test_varnish(self) :
        impl.rg_run.run_cmd("conf,start  -s varnishd -e dev,base ",self.conf)
        time.sleep(2)
        impl.rg_run.run_cmd("conf,reload,check -s varnishd -e dev,base  ",self.conf)
        impl.rg_run.run_cmd("conf,stop   -s varnishd -e dev,base ",self.conf)