from FuncUtils import tinh_khau_hao
gia_mua_moi=120000000
phi_van_chuyen=50000000
phi_lap_dat=10000000
so_nam_du_kien=10
nguyen_gia,khauhao_nam,khauhao_thang=tinh_khau_hao(
    gia_mua_moi,phi_van_chuyen,phi_lap_dat,so_nam_du_kien)
print("nguyên giá tài sản cố định =",nguyen_gia)
print("khấu hao năm =",khauhao_nam)
print("khấu hao tháng =",khauhao_thang)