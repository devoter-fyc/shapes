import argparse
p = argparse.ArgumentParser(prog="shapes",description="The shapes main.")
p.add_argument("-rs","--rendersource",action="store_true",help="Render the source of shapes")
p.add_argument("-ver","--version",action="version",version="0.1.3")
args = p.parse_args()
if args.rendersource:
    print("https://github.com/devoter-fyc/shapes")
    exit()
