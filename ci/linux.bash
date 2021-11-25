#!/bin/bash
HUGO_VERSION=0.89.4
VERSION=6.4.2.2
set -o errexit

[[ $(uname) != 'Linux' ]] && exit

pushd /tmp

urldir=https://downloadarchive.documentfoundation.org/libreoffice/old/$VERSION/deb/x86_64
filename=LibreOffice_${VERSION}_Linux_x86-64_deb

wget $urldir/${filename}.tar.gz
tar xvf ${filename}.tar.gz
dpkg -i Lib*_Linux_x86-64*deb*/DEBS/*.deb

twodigitsversion=$(echo $VERSION | cut -c 1-3)
ln -sf /opt/libreoffice${twodigitsversion}/program /tmp/program


wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.deb
dpkg -i hugo_${HUGO_VERSION}_Linux-64bit.deb