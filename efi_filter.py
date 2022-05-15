'''
__Author__	: PM
__Desc__	: Sample program to identify an EFI file and its type
__Date__	: 15/05/2022
'''
import pefile

# Change the following to db if lookup needs scale up
_file_header_lookup = {'Machine':{700:'EFI byte code'}}
_optional_header_lookup = {'Subsystem': {10: 'EFI Application', 11: 'EFI driver with boot service', 12: 'EFI driver with run-time services', 13: 'EFI ROM image'}} 


def _check_efi(file):
	pe = pefile.PE(file)
	pe_machine = pe.FILE_HEADER.Machine
	pe_subsystem = pe.OPTIONAL_HEADER.Subsystem
	for field in _file_header_lookup.keys():
		if pe_machine in _file_header_lookup[field].keys():
			print(_file_header_lookup[field][pe_machine])
			return True
	for  field in _optional_header_lookup.keys():
		if pe_subsystem in _optional_header_lookup[field].keys():
			print(_optional_header_lookup[field][pe_subsystem])
			return True
	return False
	
def main():
    file_2 = './FileZilla_3.58.0_win64_sponsored-setup.exe'
    file_4 = 'snponly.efi'
    file_5 = 'linux'
    file_6 = './ipxe.efi'
    file_7 = './PXEBCD'
    if(not _check_efi(file_7)):
    	print('Not EFI file')

if __name__ == "__main__":
    main()

	
