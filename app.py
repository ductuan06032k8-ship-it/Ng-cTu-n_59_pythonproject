import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title("📊 Ứng dụng Quản lý và Thống kê Điểm Sinh viên")

# 1. Tạo dữ liệu và DataFrame
data = {
    "Ho_ten": [
        "Ngô Đức Tuân",
        "Bùi Minh Đức",
        "Nguyễn Hữu Trung",
        "Lê Minh Trung",
        "Phạm Anh Khoa",
        "Nguyễn Tùng Lâm",
        "Đỗ Lân Phương",
        "Trần Thanh Sơn",
        "Phạm Ngọc Đăng Khôi",
        "Võ Hữu Hoàng Lâm"
    ],
    "Chuyen_can": [10, 9.5, 9.0, 8.5, 8.0, 8.5, 9.0, 9.5, 9.0, 8.0],
    "Giua_ki": [10, 9.5, 9.0, 8.5, 8.0, 7.5, 8.0, 8.5, 9.0, 8.5],
    "Cuoi_ki": [9.5, 9.0, 8.5, 10, 7.5, 8.0, 9.0, 8.5, 9.0, 9.5],
}

df = pd.DataFrame(data)
df.index = range(1, len(df) + 1)

# 2. Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ki"]
    + 0.5 * df["Cuoi_ki"]
)

# 3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Hiển thị bảng dữ liệu trên Streamlit
st.subheader("📋 Bảng điểm chi tiết của sinh viên")
st.dataframe(df.round(2), use_container_width=True)

# 4. Thống kê điểm sinh viên
st.subheader("📈 Thống kê chung")
diem_trung_binh = df["Tong_ket"].mean()
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum()

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Điểm trung bình của lớp", value=f"{diem_trung_binh:.2f}")
    st.metric(label="Số sinh viên đạt (>= 5)", value=so_sinh_vien_dat)

with col2:
    st.markdown(f"**🌟 Sinh viên cao điểm nhất:**")
    st.write(f"- Họ tên: **{sv_cao_nhat['Ho_ten']}**")
    st.write(f"- Điểm: {sv_cao_nhat['Tong_ket']:.2f} ({sv_cao_nhat['Xep_loai']})")
    
    _ = st.markdown(f"**⚠️ Sinh viên thấp điểm nhất:**")
    st.write(f"- Họ tên: **{sv_thap_nhat['Ho_ten']}**")
    st.write(f"- Điểm: {sv_thap_nhat['Tong_ket']:.2f} ({sv_thap_nhat['Xep_loai']})")

# 5. Vẽ biểu đồ điểm tổng kết
st.subheader("📊 Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"], color="skyblue")
ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN", fontsize=14, fontweight="bold")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
plt.xticks(rotation=45, ha="right")
ax.set_ylim(0, 10)
plt.tight_layout()

# Hiển thị biểu đồ trong Streamlit
st.pyplot(fig)
