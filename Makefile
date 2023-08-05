install_deps:
	bundle install

preview:
	bundle exec jekyll serve --drafts --livereload --incremental
	rm -rf _site
