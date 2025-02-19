from tests.conftest import *
import pandas
import pytest

def testDataTabularTOpathFilenameDelimitedBasic(dataframeSample: pandas.DataFrame, pathTmpTesting: pathlib.Path) -> None:
	"""Test basic functionality with DataFrame data."""
	pathOutput = pathTmpTesting / "output.csv"

	# Convert DataFrame to rows and columns
	tableRows = dataframeSample.values.tolist()
	tableColumns = dataframeSample.columns.tolist()

	dataTabularTOpathFilenameDelimited(
		pathFilename=pathOutput,
		tableRows=tableRows,
		tableColumns=tableColumns,
		delimiterOutput=','
	)

	assert pathOutput.exists()
	dfRead = pandas.read_csv(pathOutput)
	pandas.testing.assert_frame_equal(dataframeSample, dfRead)

@pytest.mark.parametrize("delimiterOutput,filenameInfix", [
	(',', 'comma'),
	('\t', 'tab'),
	('|', 'pipe')
])
def testDataTabularTOpathFilenameDelimitedDelimiters(dataframeSample: pandas.DataFrame, pathTmpTesting: pathlib.Path, delimiterOutput: Literal[','] | Literal['\t'] | Literal['|'], filenameInfix: Literal['comma'] | Literal['tab'] | Literal['pipe']) -> None:
	"""Test with different delimiters."""
	pathOutput = pathTmpTesting / f"output_{filenameInfix}.txt"

	dataTabularTOpathFilenameDelimited(
		pathFilename=pathOutput,
		tableRows=dataframeSample.values.tolist(),
		tableColumns=dataframeSample.columns.tolist(),
		delimiterOutput=delimiterOutput
	)

	assert pathOutput.exists()
	dfRead = pandas.read_csv(pathOutput, sep=delimiterOutput)
	pandas.testing.assert_frame_equal(dataframeSample, dfRead)

def testDataTabularTOpathFilenameDelimitedNoHeaders(dataframeSample: pandas.DataFrame, pathTmpTesting: pathlib.Path) -> None:
	"""Test writing data without column headers."""
	pathOutput = pathTmpTesting / "no_headers.csv"

	dataTabularTOpathFilenameDelimited(
		pathFilename=pathOutput,
		tableRows=dataframeSample.values.tolist(),
		tableColumns=[],
		delimiterOutput=','
	)

	assert pathOutput.exists()
	with open(pathOutput, 'r') as readStream:
		lines = readStream.readlines()
		assert len(lines) == len(dataframeSample)

def testDataTabularTOpathFilenameDelimitedEmptyData(pathTmpTesting: pathlib.Path) -> None:
	"""Test writing empty data."""
	pathOutput = pathTmpTesting / "empty.csv"

	dataTabularTOpathFilenameDelimited(
		pathFilename=pathOutput,
		tableRows=[],
		tableColumns=['col1', 'col2'],
		delimiterOutput=','
	)

	assert pathOutput.exists()
	with open(pathOutput, 'r') as readStream:
		lines = readStream.readlines()
		assert len(lines) == 1
		assert lines[0].strip() == 'col1,col2'

@pytest.mark.parametrize("pathStart,pathTarget,expectedResult", [
	("dir1", "dir2", "../dir2"),
	("dir1/subdir1", "dir2/subdir2", "../../dir2/subdir2"),
	("dir1", "dir1/subdir1", "subdir1"),
	("dir3/subdir3", "dir1/file1.txt", "../../dir1/file1.txt"),
])
def testFindRelativePath(setupDirectoryStructure: Any, pathStart: Literal['dir1'] | Literal['dir1/subdir1'] | Literal['dir3/subdir3'], pathTarget: Literal['dir2'] | Literal['dir2/subdir2'] | Literal['dir1/subdir1'] | Literal['dir1/file1.txt'], expectedResult: Literal['../dir2'] | Literal['../../dir2/subdir2'] | Literal['subdir1'] | Literal['../../dir1/file1.txt']) -> None:
	"""Test findRelativePath with various path combinations."""
	pathStartFull = setupDirectoryStructure / pathStart
	pathTargetFull = setupDirectoryStructure / pathTarget

	resultPath = findRelativePath(pathStartFull, pathTargetFull)
	assert resultPath == expectedResult

def testFindRelativePathWithNonexistentPaths(pathTmpTesting: pathlib.Path) -> None:
	"""Test findRelativePath with paths that don't exist."""
	pathStart = pathTmpTesting / "nonexistent1"
	pathTarget = pathTmpTesting / "nonexistent2"

	resultPath = findRelativePath(pathStart, pathTarget)
	assert resultPath == "../nonexistent2"

def testFindRelativePathWithSamePath(pathTmpTesting: pathlib.Path) -> None:
	"""Test findRelativePath when start and target are the same."""
	pathTest = pathTmpTesting / "testdir"
	pathTest.mkdir()

	resultPath = findRelativePath(pathTest, pathTest)
	assert resultPath == "."

# @pytest.mark.parametrize("pathStartStr,pathTargetStr", [
#	 ("../outside", "dir1"),
#	 ("dir1", "../outside"),
# ])
# def testFindRelativePathOutsideBase(setupDirectoryStructure, pathStartStr, pathTargetStr):
#	 """Test findRelativePath with paths outside the base directory."""
#	 pathStart = setupDirectoryStructure / pathStartStr
#	 pathTarget = setupDirectoryStructure / pathTargetStr

#	 with pytest.raises(ValueError):
#		 findRelativePath(pathStart, pathTarget)
