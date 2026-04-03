# PixMark: Copyright Protection for Images using Visual Cryptography

## Overview

**PixMark** is a Python-based project for embedding and verifying watermarks in images using non-expanding and non-degrading visual cryptography. It allows content creators to protect their images with a secure watermark and verify ownership in case of disputes.

This system consists of two main phases:

1. **Phase 1 – Watermark Embedding**  
   - Input: Original image and a binary logo/watermark  
   - Output: Watermarked image and owner share (key)  
   - Process:  
     1. Generate random binary shares of the watermark  
     2. Scramble the original image  
     3. Embed shares into the scrambled image  
   - Users can **download the watermarked image** and the **owner share**.

2. **Phase 2 – Copyright Verification**  
   - Input: Suspect image, owner share, and original logo  
   - Output: Retrieved watermark and verification result  
   - Process:  
     1. Extract shares from suspect image  
     2. Reconstruct the watermark using owner share  
     3. Compute similarity with the original watermark  
   - Displays **verification result** and **similarity score**.  

## Features

- Non-degrading watermark embedding  
- Owner share acts as a secure key for verification  
- Phase-wise separation of embedding and verification  
- Web-based frontend for easy upload and download  
- Supports **TIFF images** for high-quality watermarking  
