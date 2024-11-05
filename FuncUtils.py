def tinh_khau_hao(gia_mua,phi_vanchuyen,chi_phi_lapdat,so_nam):
    nguyen_gia = gia_mua + phi_vanchuyen + chi_phi_lapdat
    khauhao_nam = nguyen_gia /so_nam
    khauhao_nam=round(khauhao_nam,2)
    khauhao_thang = khauhao_nam /12
    khauhao_thang = round(khauhao_thang,2)
    return  nguyen_gia,khauhao_nam,khauhao_thang
def tinh_chitiet_khau_hao(gia_mua,phi_vanchuyen,chi_phi_lapdat,so_nam):
    nguyen_gia = gia_mua + phi_vanchuyen + chi_phi_lapdat
    khauhao_nam = nguyen_gia/so_nam
    chi_tiet =""
    khauhao_luyke = 0
    for nam in range (1, so_nam+1):
        if nam == so_nam:
            khauhao_nam=nguyen_gia-khauhao_luyke
        khauhao_luyke+=khauhao_nam
        chi_tiet+=f"Năm{nam}: còn lại : {nguyen_gia - khauhao_luyke:.2f}\n"
    return chi_tiet