{ nixpkgs, pynix, }:
let
  make_bundle = commit: sha256:
    let
      raw_src = builtins.fetchTarball {
        inherit sha256;
        url =
          "https://gitlab.com/dmurciaatfluid/arch_lint/-/archive/${commit}/arch_lint-${commit}.tar";
      };
      src = import "${raw_src}/build/filter.nix" nixpkgs.nix-filter raw_src;
    in import "${raw_src}/build" {
      inherit nixpkgs pynix src;
      scripts = { run-lint = [ ]; };
    };
in {
  "v4.0.1" = make_bundle "19063045573210941e5e024218fe503e83473ad4"
    "sha256:0ml1i1l0wlc3acyxx39l9b85wxclzr8y1aqidywfkcywkv89krll";
}
