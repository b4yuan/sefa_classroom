# notes on tags

### 1. student pushes submission to their repository
### 2. student would like to submit this submission and so creates a tag for submission. maybe the name of this tag will be specified by us?
	-> git tag [tag name]
	-> (git show) shows all tags in use
	-> git push origin [tag name]
tags must be pushed directly to the server, a push of the repository will not include the tags.
### 2a. let's say the student tags a version, then edits code and wants to tag again to submit an updated version (still before deadline)
	-> git tag [tag name] -f (this will force the tag to update)
	-> git push origin [tag name] -f
	to delete a tag:
	-> git tag -d [tag name]
	or:
	-> git push -d origin [tag name]
### 3. we pull tagged version of student's submission
	-> git clone -b [tag name] [repository]
if there is no tag it will have an error so we will need to include a catch for that
### 3b. get information of date of tag
	-> git log --tags --simplify-by-decoration --pretty="format:%ai %d" (this will get date of all tags)
	-> git log -1 --format=%ai [tag name] (date of only specified tag)

**scenario 1:**
- let's say student submits at 11:30 pm with tag final_ver. tag shows it was created at 11:30 pm
- then re-submits with tag at 12:05 am (after deadline). the tag will now show that it was created at 12:05 am
- then at 3 am the tagged repository is cloned for grading
- it will appear as if the student submitted after the deadline and they will lose points. so this will need to be told to the students so that they don't do this. 
 
**scenario 2:**
- there is a way to create tags from previous commits. however, the creation date of the tag will show as the date of the commit, not when the tag was created. 
- so let's say a student finishes their code and commits it at 11:30 pm, but they don't add a tag to it. the deadline passes at midnight. then at 2 am, they realize they didn't tag it. 
- they can go in and create the tag right then based on the 11:30pm commit and it will show that the tag was created at 11:30pm. so at 3 am when all code is cloned, it will clone theirs as well. 
