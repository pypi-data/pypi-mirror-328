//===----------------------------------------------------------------------===//
//
// Copyright (C) 2022 Sophgo Technologies Inc.  All rights reserved.
//
//===----------------------------------------------------------------------===//


#ifndef PPL_FE_DIALECT_PPL_TRANSFORMS_PASSES_H_
#define PPL_FE_DIALECT_PPL_TRANSFORMS_PASSES_H_

#include "mlir/Pass/Pass.h"

namespace mlir {
namespace ppl {
namespace fe {

// for frontend
std::unique_ptr<Pass> createLoopRestructurePass();
std::unique_ptr<Pass> createCanonicalizeForPass();
std::unique_ptr<Pass> replaceAffineCFGPass();
std::unique_ptr<Pass> createMem2RegPass();
std::unique_ptr<Pass> createToPPLPass();
std::unique_ptr<Pass> createInlinePass();

} // namespace fe
} // namespace ppl

#define GEN_PASS_REGISTRATION
#include "ppl/Dialect/PplFe/Transforms/Passes.h.inc"

} // namespace mlir

#endif
