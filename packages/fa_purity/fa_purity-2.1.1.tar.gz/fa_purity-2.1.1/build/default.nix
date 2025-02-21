{ nixpkgs, pynix, src, scripts, }:
let
  deps = import ./deps { inherit nixpkgs pynix; };
  pkgDeps = {
    runtime_deps = with deps.python_pkgs; [
      deprecated
      more-itertools
      simplejson
      types-deprecated
      types-simplejson
    ];
    build_deps = with deps.python_pkgs; [ flit-core ];
    test_deps = with deps.python_pkgs; [ arch-lint mypy pytest pylint ruff ];
  };
  bundle = pynix.stdBundle { inherit pkgDeps src; };
  devShell = (pynix.vscodeSettingsShell {
    pythonEnv = bundle.env.dev;
    extraPackages = [ scripts.run-lint ];
  }).shell;
in bundle // { inherit devShell; }
