"""
Purpose: Make it easier and less annoying to create posts.
Usage:

python createpost.py "Name of my title" (--isDraft)

This must be run in the home directory of this github website.

"""

import argparse
import os
import sys
from datetime import datetime

CONTENT_DIR = "content/"
JEKYLL_POST_DIR = "_posts/"

parser = argparse.ArgumentParser(allow_abbrev=False)
parser.add_argument("title", help="Title of the post. Include spaces.")
parser.add_argument("--isDraft", 
	help="If this post is a draft (unpublished). Default is false.",
	action="store_true", default=False)
parser.add_argument("--overridePost", default=False, action="store_true",
	help="Override any existing posts with same name.")


def format_title(title):
	title = title.lower()
	return title.replace(" ", "-") + ".md"

def get_date():
	return datetime.today().strftime('%Y-%m-%d')

def get_abs_path(title, isDraft):
	return os.path.join(JEKYLL_POST_DIR, get_rel_path(title, isDraft))

def get_rel_path(title, isDraft):
	relPath = os.path.join(CONTENT_DIR, format_title(title))
	return relPath

def check_file_exists(title, isDraft, overridePost):
	if os.path.exists(get_abs_path(title, isDraft)) and not overridePost:
		print("This file already exists. Please choose another post title or use --overridePost.")
		sys.exit(1)
	elif overridePost:
		print("Overriding post: %s" % title)

def get_header(title, isDraft):
	header = """---
layout: post
date: %s
title: "%s"
categories:
is_draft: %s
---

{%% include_relative %s %%}""" % (get_date(), title, str(isDraft), get_rel_path(title, isDraft))
	return header


if __name__ == "__main__":
	args = parser.parse_args()
	check_file_exists(args.title, args.isDraft, args.overridePost)
	date = get_date()
	header = get_header(args.title, args.isDraft)
	mainPostFile = os.path.join(JEKYLL_POST_DIR, "%s-%s" % (date, format_title(args.title)))
	with open(mainPostFile, "w+") as f:
		f.write(header)
	with open(get_abs_path(args.title, args.isDraft), "a+") as f:
		TEMPLATE = """Quick tips: 
images:   ![alt_text](/assets/image_name.png){:.center-image}
links:    [link_text](url)
eqn:      $x$ for inline, $$x$$ for centered
red:      <div class="red">text</div>"""
		f.write(TEMPLATE)
	print("Files created successfully!")
	print("The file that Jekyll cares about is at: %s" % mainPostFile)
	print("The file to put content in is at: %s" % get_abs_path(args.title, args.isDraft))
	print("Only the content file needs to be modified, as a pure markdown file.")
	
