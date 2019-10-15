import os

class Utilities:
    """
    Namespace class for misc system utility methods.
    """

    def basename_of(self, path) -> str:
        """
        Returns the basename of a path/name WITHOUT an extension.
        ex: "directory/file.pdf" -> "file"

        @param path(str): path/name of the file
        @return (str): an extension-less basename
        """

        return os.path.splitext(os.path.basename(str(path)))[0]

    
    def create_directory(self, path) -> bool:
        """
        Create a directory (if it doesn't exist).

        @param path(str): relative path to the directory
        @return (bool): whether creating the directory was successful or not
        """

        if not os.path.exists(path):

                try:
                        os.makedirs(path)
                except FileExistsError:
                        pass
                except:
                        return False

        return True

    
    def is_cpu_over(limit) -> bool:
        """
        Checks all CPU cores n times then gets the average.
        If the average is too high, it'll return True.

        @param limit(int): desired limit for cpu check
        @return (bool): whether the usage average is too high or not
        """
        
        percentages = []
        is_maxed_out = False

        for i in range(10):
                
                for percentage in psutil.cpu_percent(interval=0.5, percpu=True):
                        percentages.append(percentage)

        # get the average percentage of all values combined
        average = sum(percentages) / len(percentages)

        # if average percentage is over 60%, return True
        is_maxed_out = average > limit

        return is_maxed_out
