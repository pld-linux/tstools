Summary:	Command line tools for working with MPEG streams
Name:		tstools
Version:	1.11
Release:	1
License:	MPL v1.1
Group:		Applications/Networking
Source0:	http://tstools.googlecode.com/files/%{name}-1_11.tgz
# Source0-md5:	2650a09f828b19bb22829a7828f13cde
URL:		http://tstools.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tools are focussed on:
* Quick reporting of useful data (tsinfo, stream_type)
* Giving a quick overview of the entities in the stream (esdots, psdots)
* Reporting on TS packets (tsreport) or ES units/frames/fields (esreport)
* Simple manipulation of stream data (es2ts, esfilter, esreverse, esmerge, ts2es)
* Streaming of data, possibly with introduced errors (tsplay)

%prep
%setup -q
%{__sed} -e 's/libtstools.a/libtstools.so/' -i Makefile
%{__sed} -e 's/$(LIB): $(LIB)($(OBJS))/$(LIB): $(OBJS)\n	$(CC) -shared $(CFLAGS) $(OBJS) -o $@/' -i Makefile

%build
%{__make} -j1 \
	OPTIMISE_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/lib%{name}.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc data docs/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib%{name}.so
