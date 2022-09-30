# Generated by go2rpm 1.8.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/sahilm/fuzzy
%global goipath         github.com/sahilm/fuzzy
Version:                0.1.0

%gometa -f

%global common_description %{expand:
Go library that provides fuzzy string matching optimized for filenames and code
symbols in the style of Sublime Text, VSCode, IntelliJ IDEA et al.}

%global golicenses      LICENSE
%global godocs          _example CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go library that provides fuzzy string matching

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog