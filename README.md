# devops-netology
devops-10 student

HW-2.4. Инструменты Git

п.1:
git show 'aefea'

commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545
Author: Alisdair McDiarmid <alisdair@users.noreply.github.com>
Date:   Thu Jun 18 10:29:58 2020 -0400

    Update CHANGELOG.md

п.2
git show 8502                                                                                                                   
error: short SHA1 8502 is ambiguous
hint: The candidates are:
hint:   85024d310 commit 2020-03-05 - v0.12.23
hint:   8502f202c blob

git show 85024d3
commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23)

п.3
git log --all --graph b8d720
И в результатах ищем требуемый коммит

У merge-коммита b8d720f83 2 родителя:
9ea88f22f
56cd7859e

п.4
git log --pretty=oneline  v0.12.23...v0.12.24

b14b74c4939dcab573326f4e3ee2a62e23e12f89 [Website] vmc provider links
3f235065b9347a758efadc92295b540ee0a5e26e Update CHANGELOG.md
6ae64e247b332925b872447e9ce869657281c2bf registry: Fix panic when server is unreachable
5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 website: Remove links to the getting started guide's old location
06275647e2b53d97d4f0a19a0fec11f6d69820b5 Update CHANGELOG.md
d5f9411f5108260320064349b757f55c09bc4b80 command: Fix bug when using terraform login on Windows
4b6d06cc5dcb78af637bbb19c198faff37a066ed Update CHANGELOG.md
dd01a35078f040ca984cdd349f18d0b67e486c35 Update CHANGELOG.md
225466bc3e5f35baa5d07197bbc079345b77525e Cleanup after v0.12.23 release

п.5:
git log --all -S 'func providerSource('

8c928e83589d90a031f811fae52a81be7153e82f

п.6
git log --all -S 'globalPluginDirs'

commit 35a058fb3ddfae9cfee0b3893822c9a95b920f4c
Author: Martin Atkins <mart@degeneration.co.uk>
Date:   Thu Oct 19 17:40:20 2017 -0700

    main: configure credentials from the CLI config file

commit c0b17610965450a89598da491ce9b6b5cbd6393f
Author: James Bardin <j.bardin@gmail.com>
Date:   Mon Jun 12 15:04:40 2017 -0400

    prevent log output during init

    The extra output shouldn't be seen by the user, and is causing TFE to
    fail.

commit 8364383c359a6b738a436d1b7745ccdce178df47
Author: Martin Atkins <mart@degeneration.co.uk>
Date:   Thu Apr 13 18:05:58 2017 -0700

п.7
git log --all -S 'synchronizedWriters'

git show 5ac311e2a91e381e2f52234668b49ba670aa0fe5

commit 5ac311e2a91e381e2f52234668b49ba670aa0fe5
Author: Martin Atkins <mart@degeneration.co.uk>
