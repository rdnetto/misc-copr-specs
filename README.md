# Misc COPR Specs
Spec files for miscellaneous packages that were not present on COPR.

Fasd: ![](https://copr.fedorainfracloud.org/coprs/rdnetto/fasd/package/fasd/status_image/last_build.png)
Powerline-hs: ![](https://copr.fedorainfracloud.org/coprs/rdnetto/powerline-hs/package/powerline-hs/status_image/last_build.png)

### Method
- create template with `rpmdev-newspec --macros foo.spec`
- test with `rpmbuild -bb foo.spec`
- push changes and create in COPR with:
     copr-cli add-package-scm \
        --name $PKG \
        --clone-url https://github.com/rdnetto/misc-copr-specs.git \
        --subdir $PKG \
        --spec $PKG.spec \
        --webhook-rebuild on \
        $PKG
- see [here](https://copr.fedorainfracloud.org/coprs/rdnetto/$PROJECT/integrations/) for how to enable webhook integration
- manually trigger a rebuild using [this](https://copr.fedorainfracloud.org/coprs/rdnetto/$PROJECT/packages/), which will autopopulate the build form with your usual settings

# Cheat sheet
- install dependencies with `dnf builddep foo.spec`
- fetch sources with `spectool -gR foo.spec`
- check macro evaluation with `rpmspec -P foo.spec`
- view spec files for existing packages with `rpmrebuild -ps - foo.rpm` (This is a generated version, and not the same as the original.)

### Useful links
- [Offical RPM docs](http://rpm.org/documentation.html)
- [Fedora packaging guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/)
- [Packaging Guide](https://rpm-packaging-guide.github.io/#what-is-a-spec-file)
- [List of macros](http://rpm.org/user_doc/macros.html)
- [Cheat sheet](https://ro-che.info/articles/2018-01-25-rpm-packager-cheat-sheet)

