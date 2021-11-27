from src import app
from src import ma
import argparse
from src.config import FactoryConfigClass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="input arguments")
    parser.add_argument("-env", "--environment", help="environment name: prod, qa, or dev", type=str,
                        required=False, default='dev')
    args = parser.parse_args()
    ma.init_app(app=app)
    app.config.from_object(FactoryConfigClass(env=args.environment))
    app.run('0.0.0.0', 5000, debug=True, threaded=True, use_reloader=True)
