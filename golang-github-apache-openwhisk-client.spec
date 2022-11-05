# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/apache/openwhisk-client-go
%global goipath         github.com/apache/openwhisk-client-go
Version:                1.2.0
%global tag             1.2.0
%global commit          18a6a867dd6fe81ad60ebb4dc65eb284e98ca9df

%gometa -f

%global common_description %{expand:
Go client library for the Apache OpenWhisk platform.}

%global golicenses      NOTICE.txt LICENSE.txt
%global godocs          example CONTRIBUTING.md CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go client library for the Apache OpenWhisk platform

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
# Remove dependency on deprecated JibberJabberDetector
# JibberJabberDetector was meant to be use for Locale detection, but code
# is not complete, as always returns DEFAULT_LOCALE
# https://github.com/apache/openwhisk-client-go/blob/master/wski18n/i18n.go#L65
sed -i -e 's/Init(new(JibberJabberDetector))/DEFAULT_LOCALE/' wski18n/i18n.go
sed -i -e 's/detector Detector//' wski18n/i18n.go
sed -i -e 's/Locale(detector)/DEFAULT_LOCALE/' wski18n/i18n.go
rm wski18n/detection.go

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
