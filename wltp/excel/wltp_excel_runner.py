#!python#-*- coding: utf-8 -*-"""Sample `xlwings` script####################### The functions included provide for running a batch of experiments in an excel-table with json-pointer paths as headers (see accompanying :file:`.xlsm`).You can debug it by running it directly as a python script, as suggested by :   http://docs.xlwings.org/debugging.html<< EDIT THIS SCRIPTTO PUT YOUR EXCEL/XLWINGS PYTHON-CODE, BELOW >>"""from __future__ import division, print_function, unicode_literalsimport loggingimport osfrom wltp.experiment import Experimentimport pandas as pdimport wltp.pandel as pdlimport xlwings as xwdef _init_logging(loglevel):    logging.basicConfig(level=loglevel)    logging.getLogger().setLevel(level=loglevel)_init_logging(logging.INFO)log = logging.getLogger(__name__) def add_cycle_run_as_sheet(veh_id, mdl_out):    sheet = "cycle_%s"%veh_id    try:        xw.Sheet.add(sheet)    except Exception as ex:        log.info("Sheet(%s) already exists(%s).", sheet, ex)        xw.Sheet(sheet).clear()    xw.Range(sheet, 'A1').value = mdl_out['cycle_run']        def read_table_as_df(range):    """    Expects excel-table with jsonpointer paths as Header and 1st column named `id` as index,     like this::            id     vehicle/test_mass  vehicle/p_rated           vehicle/gear_ratios         veh_1               1500              100  [120.75, 75, 50, 43, 37, 32]         veh_2               1600               80  [120.75, 75, 50, 43, 37, 32]         veh_3               1200               60  [120.75, 75, 50, 43, 37, 32]             """    vehs = xw.Range(range).table.value    vehs = pd.DataFrame(vehs[1:], columns=vehs[0]).set_index('id')        return vehsdef build_models(vehs_df):    """    Builds all input-dataframes as Experiment classes and returns them in a list of (veh_id, exp) pairs.        :param vehs_df:     A dataframe indexed by veh_id, and with columns *json-pointer* paths into the model    :return: a list of (veh_id, :class:`wltp.experiment.Experiment`) tuples    """    experiment_pairs = []    for veh_id, row in vehs_df.iterrows():        try:            mdl_in = {}            for k, v in row.items():                log.debug('veh_id(%s): Column(%s): %s', veh_id, k, v)                if not v:                    continue                if isinstance(v, str):                    v = eval(v)                pdl.set_jsonpointer(mdl_in, k, v)                        exp = Experiment(mdl_in)                        experiment_pairs.append((veh_id, exp))        except Exception as ex:            raise Exception('Invalid model for vehicle(%s): %s' % (veh_id, ex)) from ex             return experiment_pairsdef run_experiments(experiment_pairs):    """    Iterates `veh_df` and runs experiment_pairs.        :param vehs_df:     A dataframe indexed by veh_id, and with columns *json-pointer* paths into the model    """    for veh_id, exp in experiment_pairs:        try:            mdl_out = exp.run()                        add_cycle_run_as_sheet(veh_id, mdl_out)        except Exception as ex:            raise Exception('Experiment failed for vehicle(%s): %s' % (veh_id, ex)) from ex         if __name__ == '__main__':    ## Open and run experiments    #    log.info('CWD: %s', os.getcwd())    excel_fname = os.path.join(os.path.dirname(__file__), '%s.xlsm' % os.path.splitext(os.path.basename(__file__))[0])    wb_path = os.path.abspath(excel_fname)    xw.Workbook(wb_path)        vehs_df = read_table_as_df('D2')    log.info('%s', vehs_df)    exp_pairs = build_models(vehs_df)    run_experiments(exp_pairs)        