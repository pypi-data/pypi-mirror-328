#!/usr/bin/env python
"""
_StageOutImpl_

Interface for Stage Out Plugins. All stage out implementations should
inherit this object and implement the methods accordingly

"""
from __future__ import print_function

from builtins import range

import logging
import os
import time

from WMCore.Storage.Execute import runCommandWithOutput
from WMCore.Storage.StageOutError import StageOutError


class StageOutImpl:
    """
    _StageOutImpl_

    Define the interface that needs to be implemented by stage out
    plugins

    Object attributes:

    - *numRetries* : Number of automated retry attempts if the command fails
                     default is 3 attempts
    - *retryPause* : Time in seconds to wait between retries.
                     default is 10 minutes
    """

    def __init__(self, stagein=False):
        self.numRetries = 3
        self.retryPause = 600
        self.stageIn = stagein

    @staticmethod
    def splitPFN(pfn):
        """
        _splitPFN_

        Generic function to split the PFN in smaller pieces, such as:
        { <protocol>, <host>, <path>, <opaque> }
        """
        protocol = pfn.split(':')[0]
        host = pfn.split('/')[2]
        thisList = pfn.replace('{}://{}/'.format(protocol, host), '').split('?')
        path = thisList[0]
        opaque = ""
        # If we have any opaque info keep it
        if len(thisList) == 2:
            opaque = "?{}".format(thisList[1])

        # check for the path to actually be in the opaque information
        if opaque.startswith("?path="):
            elements = opaque.split('&')
            path = elements[0].replace('?path=', '')
            buildingOpaque = '?'
            for element in elements[1:]:
                buildingOpaque += element
                buildingOpaque += '&'
            opaque = buildingOpaque.rstrip('&')
        elif opaque.find("&path=") != -1:
            elements = opaque.split('&')
            buildingOpaque = elements[0]
            for element in elements[1:]:
                if element.startswith('path='):
                    path = element.replace('path=', '')
                else:
                    buildingOpaque += '&' + element
            opaque = buildingOpaque
        return protocol, host, path, opaque

    def executeCommand(self, command):
        """
        _execute_

        Execute the command provided, throw a StageOutError if it exits
        non zero

        """
        try:
            exitCode, output = runCommandWithOutput(command)
            msg = "Command exited with status: {}\nOutput message: {}".format(exitCode, output)
            logging.info(msg)
        except Exception as ex:
            raise StageOutError(str(ex), Command=command, ExitCode=60311) from ex

        if exitCode:
            msg = "Command exited non-zero, ExitCode: {}\nOutput: {}".format(exitCode, output)
            formatted_msg = "Exception During Stage Out:\n{}".format(msg)
            logging.error(formatted_msg)
            raise StageOutError(msg, Command=command, ExitCode=exitCode)

    def createSourceName(self, protocol, pfn):
        """
        _createSourceName_

        construct a source URL/PFN for the pfn provided based on the
        protocol that can be passed to the stage command that this
        implementation uses.

        """
        raise NotImplementedError("StageOutImpl.createSourceName")

    def createTargetName(self, protocol, pfn):
        """
        _createTargetName_

        construct a target URL/PFN for the pfn provided based on the
        protocol that can be passed to the stage command that this
        implementation uses.

        By default this is the same as createSourceName (in cases
        of stage ins the 'local' file is the target). Override this
        in your implementation of this is not the case.

        """
        return self.createSourceName(protocol, pfn)

    def createOutputDirectory(self, targetPFN):
        """
        _createOutputDirectory_

        If a seperate step is required to create a directory in the
        SE for the stage out PFN provided, do that in this command.

        If no directory is required, do not implement this method
        """

    def createStageOutCommand(self, sourcePFN, targetPFN, options=None, checksums=None):
        """
        _createStageOutCommand_

        Build a shell command that will transfer the sourcePFN to the
        targetPFN using the options provided if necessary

        """
        raise NotImplementedError("StageOutImpl.createStageOutCommand")

    def createDebuggingCommand(self, sourcePFN, targetPFN, options=None, checksums=None):
        """
        Build a shell command that will report in the logs the details about
        failing stageOut commands
        """
        raise NotImplementedError("StageOutImpl.createDebuggingCommand")

    def removeFile(self, pfnToRemove):
        """
        _removeFile_

        Construct and issue the command to remove the PFN provided as
        this impl requires.
        This will be used by the cleanup nodes in merge jobs that remove the
        intermediate files upon successful completion of the merge job

        """
        raise NotImplementedError("StageOutImpl.removeFile")

    def createRemoveFileCommand(self, pfn):
        """
        return the command to delete a file after a failed copy
        """
        if pfn.startswith("/"):
            return "/bin/rm -f {}".format(pfn)
        elif os.path.isfile(pfn):
            return "/bin/rm -f {}".format(os.path.abspath(pfn))
        else:
            return ""

    def __call__(self, protocol, inputPFN, targetPFN, options=None, checksums=None):
        """
        _Operator()_

        This operator does the actual stage out by invoking the overridden
        plugin methods of the derived object.


        """
        #  //
        # // Generate the source PFN from the plain PFN if needed
        # //
        sourcePFN = self.createSourceName(protocol, inputPFN)

        # destination may also need PFN changed
        # i.e. if we are staging in a file from an SE
        targetPFN = self.createTargetName(protocol, targetPFN)
        #  //
        # // Create the output directory if implemented
        # //
        for retryCount in range(self.numRetries + 1):
            try:
                logging.info("Creating output directory...")
                self.createOutputDirectory(targetPFN)
                break
            except StageOutError as ex:
                msg = "Attempt {} to create a directory for stageout failed.\n".format(retryCount)
                msg += "Automatically retrying stage out in {} secs\n ".format(self.retryPause)
                msg += "Error details:\n{}\n".format(str(ex))
                logging.error(msg)
                if retryCount == self.numRetries:
                    #  //
                    # // last retry, propagate exception
                    # //
                    raise ex
                time.sleep(self.retryPause)

        # //
        # // Create the command to be used.
        # //
        command = self.createStageOutCommand(sourcePFN, targetPFN, options, checksums)
        #  //
        # // Run the command
        # //

        stageOutEx = None  # variable to store the possible StageOutError
        for retryCount in range(self.numRetries + 1):
            try:
                logging.info("Running the stage out...")
                self.executeCommand(command)
                break
            except StageOutError as ex:
                msg = "Attempt {} to stage out failed.\n".format(retryCount)
                msg += "Error details:\n{}\n".format(str(ex))
                logging.error(msg)
                if retryCount == self.numRetries:
                    # Last retry, propagate the information outside of the for loop
                    stageOutEx = ex
                msg += "Automatically retrying in {} secs\n ".format(self.retryPause)
                time.sleep(self.retryPause)

        # This block will now always be executed after retries are exhausted
        if stageOutEx is not None:
            logging.error("Maximum number of retries exhausted. Further details on the failed command reported below.")
            command = self.createDebuggingCommand(sourcePFN, targetPFN, options, checksums)
            self.executeCommand(command)
            raise stageOutEx from None
