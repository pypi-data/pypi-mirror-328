TEMP_NAME = os.getenv('CONFIG') or '.vntrader' # 使用第一个参数作为temp_dir的名字
TRADER_DIR, TEMP_DIR = _get_trader_dir(TEMP_NAME)
sys.path.append(str(TRADER_DIR))