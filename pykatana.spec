%define name 		pykatana
%define Summary		A python source-cutter tool
%define sourcetype      tar.gz
%define version         0.0.1

Name:         %name
Summary:       %Summary
Summary(hu):   %Summary_hu
Version:       %version
Release:       %mkrel 1
License:       GPL3
Distribution: blackPanther OS
Vendor:       blackPanther Europe
Packager:     Miklos Horvath
Group:        Development/Tools
Source0:      %name-%version.%sourcetype
Buildroot:     %_tmppath/%name-%version-%release-root

Requires:     python3 >= 3.4
Requires:     glibc >= 2.19.2

%description
The pykatana is a tool to cut the long python sources to more modules.                                                                                                                                              

%files
%defattr(-,root,root)
%_bindir/%name
%python3_sitelib/%name

%prep
%setup -q 

%build
%{__python3} setup.py build
%{__python3} setup.py build_scripts

%install
%{__python3} setup.py install --skip-build --root %{buildroot}
%{__python3} setup.py install --skip-build --no-compile --root %{buildroot}

%clean
rm -rf %buildroot


%changelog
* Tue Mar 22 2016 Miklos Horvath <mikloshorvath aattt blackpanther dooootttt hu> 
- initial version
