## 0.1.12

24aec23 Snapshot identity is optimistically calculated by the first word of the progressbar text and the position of the bar
e012306 Dont sleep in between queue reads, let the timeout parameter do the work [3]
65ac685 Allow bucket names to be overriden [2]
5e7da7a Allow metric names to be overridden [2]
146241f Added debug mode to validate output remotely
952e96c Added test cases to validate duplication in results is now resolved [1]
6d1e856 Standardised some duplicated test logic
e4357dc Split bucket name, instance and last seen #1
547f6a7 Updated release scripts to update uv lockfile

## 0.1.11

011b4fc Downgraded python dependency to 3.8. Could possibly go further

## 0.1.10

69052aa Refactor main api - Simplified properties now behaviour has been externalised - Allowed api to be picked for use in multiprocessing scenarios
2a47553 Moving metric server over to using new BucketManager
50b3d6b Cleaning up thread behaviour
01ce7f9 Monitor now async and no longer enumerates tqdm internal members
1f26c83 Separating bucket management duties
6a28026 Renamed `add` to `upsert` to better reflect bucket use
72fa6e6 No longer hold references to tqdm objects, hold only `TqdmSnapshot` instead
3685f6a Added test to assert the proxy can be passed around with multiprocessing
5b67359 (chore) linted
3cd132e Added build step to invoke uv to update the uv.lock file such that it can be committed

## 0.1.9

4bf6d05 Formatted release.py
3eb92eb Bump version in lockfile
56daf12 Run tests. Can be messy on stdout

## 0.1.8

4e9ae14 Dont emit logs to stderr
3468173 Commit uv lock file as well when releasing
8f57ae1 Fixed buckets not being accumulated correctly
bd750ae Logged bucket/instance collecting stats for each iteration

## 0.1.7

cc36993 Fixed github release details

## 0.1.6

ef9553e Added gh release step
e7b03db Release [patch] version to 0.1.5

## 0.1.4

0ec841c Added intermediate release type
5abbb1f Release [patch] version to 0.1.3

## 0.1.2

6250aec Write intermediate content to release/ directory
9aab64c Only push if allowed
babc683 Fix release diff naming
912cfc0 Adding version bump utils
e8ad6b6 Adding version bump utils
c26620a Fix url in readme
dac5257 Moved helper scripts to scripts directory
