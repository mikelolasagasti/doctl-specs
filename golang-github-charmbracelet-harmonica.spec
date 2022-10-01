# Generated by go2rpm 1.8.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/charmbracelet/harmonica
%global goipath         github.com/charmbracelet/harmonica
Version:                0.2.0

%gometa -f

%global common_description %{expand:
A simple, physics-based animation library.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A simple, physics-based animation library

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
