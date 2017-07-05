import pkg_resources

from oslo_config import cfg

# Notes: We have this feature by this code line:
# https://github.com/openstack/oslo.config/blob/a8482a323b65dd5390c4ec375b3b4b50f66bb204/oslo_config/cfg.py#L2464

_generator_opts = [
    cfg.StrOpt(
        'firstname',
        required=True,
        help='Your first name.'),
    cfg.StrOpt(
        'lastname',
        help='Your last name.'),
    cfg.IntOpt(
        'age',
        default=100,
        help='Your age.'),
]

def main(args=None):
    version = pkg_resources.get_distribution('oslo.config').version
    conf = cfg.ConfigOpts()
    conf.register_cli_opts(_generator_opts)
    conf(args, version=version)
    print("Your name: {} {}" .format(conf.firstname, conf.lastname))
    print("Your age: {}".format(conf.age))


if __name__ == '__main__':
    main()

"""
Result: 

daidv@dangvandai:~/GIT/openstack-stuffs/lib$ python oslo_config_cli_opts.py --firstname Dai --lastname "Dang Van" --age 24 
Your name: Dai Dang Van
Your age: 24
"""