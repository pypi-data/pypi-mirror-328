{ nixpkgs, pynix, }:
let
  inherit (pynix) lib;

  layer_1 = python_pkgs:
    python_pkgs // {
      arch-lint =
        let result = import ./arch_lint.nix { inherit nixpkgs pynix; };
        in result."v4.0.1".pkg;
      types-simplejson = import ./simplejson/stubs.nix lib;
    };
  python_pkgs = pynix.utils.compose [ layer_1 ] pynix.lib.pythonPackages;
in { inherit lib python_pkgs; }
